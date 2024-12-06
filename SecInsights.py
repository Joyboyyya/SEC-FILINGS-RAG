import os
import requests
from pydantic import BaseModel, ValidationError
from typing import Annotated, Literal, Optional
from datetime import datetime
from autogen import ConversableAgent, register_function
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.chains import LLMChain
import numpy as np
import pandas as pd
from io import StringIO
# import spacy
# from bs4 import BeautifulSoup
import time
import json
load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

system_message = """ 
Your task is to identify and fill the following entities from the user's prompt:

1. **ticker**: The abbreviation of the company's name.
2. **document_type**: 'Form 10K' (for annual financial details), 'Form 10Q' (for quarterly financial details), etc.
3. **year**: 
   - If 'Form 10K' is chosen, the year should be in the format 'YYYY' (e.g., 2021, 2019).
   - If 'Form 10Q' is chosen, the year should be in the format 'YYYY QX' (e.g., 2023 Q3, 2022 Q2).

User prompts may be explicit or implicit and may not specify all required entities. Use context to infer missing details.

If a user prompt is complex, you may break it into simpler, atomic prompts and provide separate outputs for each.

### Guidelines for Handling Qualitative Financial Questions:

1. **Map to Relevant Documents**: Use the most relevant financial documents (annual or quarterly reports) that are likely to contain information on market trends, growth prospects, or other qualitative aspects.

2. **Use Representative Entities**: When the user question is about a sector or general trends, use representative entities such as sector ETFs (e.g., XLK for technology) to provide the context.

3. **Infer Contextual Details**: Use the context provided in the user's question to infer missing details and make reasonable assumptions about the tickers, document types and years.

### Examples:
1. **Prompt**: "Please provide the report on recent developments at Apple."
   **Output**: 
   - ('ticker': 'AAPL', 'document_type': 'Form 10K', 'year': '2023')
   - ('ticker': 'AAPL', 'document_type': 'Form 10Q', 'year': '2023 Q3')

2. **Prompt**: "Please provide the report on third quarter for Apple for the years 2021 and 2022."
   **Output**: 
   - ('ticker': 'AAPL', 'document_type': 'Form 10Q', 'year': '2021 Q3')
   - ('ticker': 'AAPL', 'document_type': 'Form 10Q', 'year': '2022 Q3')

3. **Prompt**: "What are the prevailing market trends in the technology sector?"
   **Output**: 
   - ('ticker': 'XLK', 'document_type': 'Form 10K', 'year': '2023')  # XLK is the ticker for the Technology Select Sector SPDR Fund, commonly used to represent the technology sector.
   - ('ticker': 'XLK', 'document_type': 'Form 10Q', 'year': '2023 Q3') # Use the latest quarterly report for current trends and projections.

4. **Prompt**: "What are the growth prospects of Tesla in the next five years?"
   **Output**: 
   - ('ticker': 'TSLA', 'document_type': 'Form 10K', 'year': '2023')  # Use the most recent annual report for forward-looking statements.
   - ('ticker': 'TSLA', 'document_type': 'Form 10Q', 'year': '2023 Q3')  # Use the latest quarterly report for current trends and projections.

Return 'TERMINATE' when the task is completed.
"""

# Define the assistant agent
assistant = ConversableAgent(
    name="Assistant",
    system_message=system_message,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    max_consecutive_auto_reply=5,
    llm_config={"config_list": [{"model": "gpt-3.5-turbo-1106", "api_key": OPENAI_API_KEY}]},
    # human_input_mode="NEVER",
)

# Define the user proxy agent
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

chat_result = user_proxy.initiate_chat(
    assistant,
    message="What impact do blockchain and cryptocurrencies have on traditional financial markets?"
)