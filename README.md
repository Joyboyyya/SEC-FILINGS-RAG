### Autogen-tools

To create pgvector postrgres vector database with the name "vector_db" by following along this youtube tutorial: https://youtu.be/FDBnyJu_Ndg?si=RtJ6RxkXaEHOZXhU

Here's a summary of the functions defined in the notebook:

### Functions Summary

1. **`check_ticker_exists`**
   - **Parameters**:
     - `ticker (str)`: The ticker symbol to check.
   - **Docstring**: 
     ```plaintext
     Check if a particular ticker exists using the Financial Modeling Prep API.
     
     Parameters:
     - ticker (str): The ticker symbol to check.
     - api_key (str): Your FMP API key.
     
     Returns:
     - bool: True if the ticker exists, False otherwise.
     ```

2. **`convert_to_markdown`**
   - **Parameters**:
     - `sections (list)`: A list of sections parsed from the document.
     - `level_to_markdown (dict)`: A mapping from section levels to markdown header syntax.
   - **Docstring**: 
     ```plaintext
     Converts a list of sections into markdown format based on the section levels.
     
     Args:
         sections (list): A list of sections parsed from the document.
         level_to_markdown (dict): A mapping from section levels to markdown header syntax.
     
     Returns:
         str: The document content in markdown format.
     ```

3. **`combine_sentences`**
   - **Parameters**:
     - `sentences (list)`: A list of sentences to combine.
     - `buffer_size (int)`: The number of surrounding sentences to include for context.
   - **Docstring**: 
     ```plaintext
     Combines sentences with a specified buffer size to create context for each sentence.
     
     Args:
         sentences (list): A list of sentences to combine.
         buffer_size (int): The number of surrounding sentences to include for context.
     
     Returns:
         list: The list of sentences with combined context.
     ```

4. **`calculate_chunk_sizes`**
   - **Parameters**:
     - `sentences (list)`: A list of sentences.
     - `distances (list)`: A list of cosine distances between sentence embeddings.
     - `threshold (float)`: The distance threshold for determining chunk boundaries.
   - **Docstring**: 
     ```plaintext
     Calculates chunk sizes for a document based on distance between sentence embeddings and a threshold.
     
     Args:
         sentences (list): A list of sentences.
         distances (list): A list of cosine distances between sentence embeddings.
         threshold (float): The distance threshold for determining chunk boundaries.
     
     Returns:
         list: The list of text chunks.
     ```

5. **`find_appropriate_threshold`**
   - **Parameters**:
     - `sentences (list)`: A list of sentences.
     - `distances (list)`: A list of cosine distances between sentence embeddings.
     - `initial_threshold (float)`: The initial distance threshold.
     - `ceiling (int)`: The maximum chunk size in words.
   - **Docstring**: 
     ```plaintext
     Finds the appropriate distance threshold for creating chunks within a size ceiling.
     
     Args:
         sentences (list): A list of sentences.
         distances (list): A list of cosine distances between sentence embeddings.
         initial_threshold (float): The initial distance threshold.
         ceiling (int): The maximum chunk size in words.
     
     Returns:
         tuple: The threshold, list of chunks, and list of chunk sizes.
     ```

6. **`calculate_cosine_distances`**
   - **Parameters**:
     - `sentences (list)`: A list of sentences with combined sentence embeddings.
   - **Docstring**: 
     ```plaintext
     Calculates cosine distances between consecutive sentence embeddings.
     
     Args:
         sentences (list): A list of sentences with combined sentence embeddings.
     
     Returns:
         tuple: The list of distances and the updated list of sentences.
     ```

7. **`get_jsonparsed_data`**
   - **Parameters**:
     - `url (str)`: The URL to fetch data from.
   - **Docstring**:
     ```plaintext
     Fetches and parses JSON data from a given URL.
     
     Args:
         url (str): The URL to fetch data from.
     
     Returns:
         dict: The JSON data as a dictionary.
     ```
   - **Functionality**:
     - Opens the URL and fetches the data.
     - Reads and decodes the response data.
     - Parses the JSON data and returns it as a dictionary.

8. **`is_within_quarter`**
   - **Parameters**:
     - `date_str (str)`: The date in 'YYYY-MM' format.
     - `year (str)`: The fiscal year to check.
     - `start_month (int)`: The starting month of the quarter.
     - `end_month (int)`: The ending month of the quarter.
   - **Docstring**:
     ```plaintext
     Checks if the given date falls within the specified fiscal quarter.
     
     Args:
         date_str (str): The date in 'YYYY-MM' format.
         year (str): The fiscal year to check.
         start_month (int): The starting month of the quarter.
         end_month (int): The ending month of the quarter.
     
     Returns:
         bool: True if the date is within the fiscal quarter, False otherwise.
     ```
   - **Functionality**:
     - Splits the date string to get the year and month.
     - Checks if the date is within the specified fiscal quarter.

9. **`which_fiscal_year`**
   - **Parameters**:
     - `date_str (str)`: The filing date in 'YYYY-MM-DD' format.
     - `fiscal_year (str)`: The initial fiscal year.
   - **Docstring**:
     ```plaintext
     Determines the fiscal year for a given date.
     
     Args:
         date_str (str): The filing date in 'YYYY-MM-DD' format.
         fiscal_year (str): The initial fiscal year.
     
     Returns:
         str: The fiscal year adjusted for the filing date.
     ```
   - **Functionality**:
     - Converts the date string to a datetime object.
     - Adjusts the fiscal year based on the filing month.
     - Returns the adjusted fiscal year as a string.

10. **`truncate_tables`**
   - **Parameters**:
     - `tables (list of str)`: A list of table names to truncate.
     - `host (str)`: The hostname of the PostgreSQL server.
     - `database (str)`: The name of the database.
     - `user (str)`: The username to connect to the database.
     - `password (str)`: The password to connect to the database.
     - `cascade (bool)`: If `True`, applies the `CASCADE` option to truncate dependent tables. Default is `False`.
     - `restart_identity (bool)`: If `True`, resets any auto-increment counters in the tables. Default is `False`.
   - **Docstring**:
     ```plaintext
     Truncate one or more tables in a PostgreSQL database.
     
     Args:
         tables (list of str): List of table names to truncate.
         host (str): The hostname of the PostgreSQL server.
         database (str): The name of the database.
         user (str): The username to connect to the database.
         password (str): The password to connect to the database.
         cascade (bool): If True, apply the CASCADE option to truncate dependent tables.
         restart_identity (bool): If True, reset any auto-increment counters in the tables.
     
     Returns:
         None
     ```
   - **Functionality**:
     - Establishes a connection to the PostgreSQL database using the provided connection parameters.
     - Constructs and executes the `TRUNCATE TABLE` SQL command for the specified tables.
     - Optionally applies `CASCADE` to truncate dependent tables and `RESTART IDENTITY` to reset auto-increment counters.
     - Handles potential errors by printing an error message.
     - Closes the database connection and cursor after execution.

11. **`document_selector_downloader`** 
   - **Parameters**:
     - `ticker (str)`: The ticker symbol related to user query (e.g., AAPL, MSFT, BTC-USD). Default is "AAPL".
     - `document_type (str)`: The document type related to user query (e.g., Form 10-K, Form 10-Q, Form 8-K). Default is "Form 10-K".
     - `year (str)`: The year (format: YYYY) or quarter of the year (format: YYYY QX) related to user query (e.g., 2015, 2001, 2017 Q3). Default is "2023".

   - **Docstring**:
     ```plaintext
     Downloads and saves a specific SEC document based on the provided parameters,
     and returns the path to the saved HTML and PDF files.

     Args:
         ticker (str): The ticker symbol of the company.
         document_type (str): The type of document to download (e.g., Form 10-K, Form 10-Q).
         year (str): The year or fiscal quarter to filter documents.

     Returns:
         Tuple[str, str]: Paths to the saved HTML and PDF files.
     ```

   - **Functionality**:
     - **Fetch API Key**: Retrieves the FMP API key from environment variables.
     - **Document Type Mapping**: Maps the given document type to its respective filing type code.
     - **Quarter Mapping**: Maps fiscal quarters to their respective start and end months.
     - **Check Ticker**: Verifies if the given ticker exists using the `check_ticker_exists` function.
     - **Determine Output Directory**: Creates an output directory based on the document type and date.
     - **Check Existing Files**: Checks if the HTML and PDF files already exist to avoid redundant downloads.
     - **API Request**: Constructs the URL for the API request and fetches data from the Financial Modeling Prep (FMP) API.
     - **Filter Results**: Filters the API results based on the filing date and type.
     - **Create Output Directory**: Ensures the output directory exists.
     - **PDF and HTML Generation**:
       - Generates and saves the PDF using `pdfkit`.
       - Saves the HTML content fetched from the document URL.

   - **Returns**:
     - **Tuple[str, str]**: The paths to the saved HTML and PDF files.

   This function integrates multiple components such as API interaction, file handling, and document conversion to streamline the process of downloading and saving SEC documents based on user queries. If you need more details or further refinement, let me know!

12. **`multi_query_generator_rag_fusion`**

   - **Parameters**:
     - `input (str)`: The user's input prompt or query related to qualitative data to undergo query translation.

   - **Docstring**:
     ```plaintext
     Generates multiple search queries based on a single input prompt using the RAG-Fusion approach.

     Args:
         input (str): The user's input prompt or query for generating related search queries.

     Returns:
         List[str]: A list of generated search queries.
     ```

   - **Functionality**:
     - **Define RAG-Fusion Prompt Template**: The template provides a structured approach for generating multiple search queries based on a single input query. It involves analyzing the input query, breaking it down into different aspects or subtopics, and formulating specific search queries

.
       - **Template Breakdown**:
         - **Step 1**: Analyze the input query to understand its context.
         - **Step 2**: Break down the query into different aspects or subtopics and provide reasoning for each.
         - **Step 3**: Generate multiple specific and relevant search queries based on the identified aspects.
     - **Pipeline Definition**:
       - **Prompt Fusion**: Uses the `ChatPromptTemplate` to apply the defined template.
       - **Generate Queries**: Utilizes `ChatOpenAI` with a set temperature for consistent output and `StrOutputParser` to split the generated text into individual queries.
     - **Function Execution**:
       - Executes the `generate_queries` pipeline with the provided input.
       - Returns a list of generated search queries based on the input prompt.

   - **Example Usage**:
     ```python
     input_query = "Explain the impact of climate change on agriculture."
     generated_queries = multi_query_generator_rag_fusion(input_query)
     print(generated_queries)
     ```

   - **Output**:
     - A list of specific and relevant search queries related to the input query.

   This function leverages the RAG-Fusion approach to break down and expand a single input query into multiple detailed search queries, enhancing the user's ability to explore various aspects of the topic. If you need more details or further refinement, let me know!

13. **`process_financial_documents`**

   - **Parameters**:
     - `file_paths (str)`: Comma-separated list of paths to the financial document files.
     - `input_query (str)`: User input prompt or query related to qualitative data to undergo query translation.

   - **Docstring**:
     ```plaintext
     Processes multiple financial documents, chunks them, and stores the chunks in a single FAISS vector store.

     Args:
         file_paths (str): Comma-separated list of paths to the financial document files.
         input_query (str): User input prompt or query related to qualitative data to undergo query translation.

     Returns:
         List[str]: A list of retrieved documents based on the input query.
     ```

   - **Functionality**:
     1. **Initialize Variables**:
        - Retrieves the OpenAI API key from environment variables.
        - Sets constants for the chunking process, including `breakpoint_percentile_threshold` and `chunk_size_ceiling`.
        - Initializes empty lists for storing document chunks and retrieval results.
        - Sets up the embeddings engine using OpenAI embeddings.

     2. **Process Each File**:
        - Splits the input file paths and iterates over each path.
        - Reads the content of each file.
        - Parses the document content using `Edgar10QParser`.
        - Builds the document structure using `TreeBuilder`.
        - Determines the markdown levels for the document sections.
        - Converts the document content to markdown format.
        - Splits the markdown content into sentences.
        - Combines sentences with context.
        - Embeds the combined sentences using the embeddings engine.
        - Calculates cosine distances between sentence embeddings.
        - Finds the appropriate threshold for chunk sizes.
        - Assigns document IDs and stores the chunks.

     3. **Create FAISS Vector Store**:
        - Creates a FAISS vector store from the document chunks using the embeddings engine.
        - Checks the number of vectors in the store.

     4. **Retrieve Relevant Documents**:
        - Uses the vector store to retrieve the top k relevant documents based on the input query.
        - Reorders the documents for better relevance using `LongContextReorder`.
        - Collects and prints the retrieved documents.

   - **Returns**:
     - **List[str]**: A list of retrieved documents based on the input query.

   - **Example Usage**:
     ```python
     file_paths = "path/to/document1.html,path/to/document2.html"
     input_query = "What are the key financial highlights of the company in the latest quarter?"
     retrieved_documents = process_financial_documents(file_paths, input_query)
     print(retrieved_documents)
     ```

   - **Output**:
     - A list of relevant sections from the processed financial documents based on the input query.

   This function efficiently processes multiple financial documents, extracts and chunks their content, stores the chunks in a FAISS vector store, and retrieves relevant sections based on a user query. If you need more details or further refinement, let me know!

### Summary of the Conversable Agents

1. **Multi-Query Generator Agent**

**Agent Name**: `Multi_Query_Generator_Agent`

**Description**:
- This agent generates multiple queries based on a single input query.
- It uses the GPT-4o-mini model and does not require human input.

**System Message**: 
```plaintext
You return me the list of multiple queries from a single input query. Make a note that you should call the multi_query_generator_rag_fusion tool.
```

**Human Input Mode**: `NEVER`

---

2. **Document Downloader Agent**

**Agent Name**: `Document_Downloader_Agent`

**Description**:
- This agent selects the necessary financial documents based on the queries generated by the `Multi_Query_Generator_Agent`.
- It ensures that the required documents are downloaded if they do not already exist in the folder.
- It uses the GPT-4o-mini model and does not require human input.

**System Message**: 
```plaintext
You select the required ticker/s, financial document/s and year/s for each of the queries generated by multi_query_generator_agent and then download the required financial documents only if the document does not already exist in the folder.
```

**Human Input Mode**: `NEVER`

---

3. **Document Processor Agent**

**Agent Name**: `Document_Processor_Agent`

**Description**:
- This agent processes the downloaded financial documents.
- It collects the paths of all the required HTML financial documents, stores them in a list, and passes this list as an argument to the `process_financial_documents` tool.
- It uses the GPT-4o-mini model and does not require human input.

**System Message**: 
```plaintext
You gather all the required html financial documents' path, store it in a list and pass it as an argument to process_financial_documents tool.
```

**Human Input Mode**: `NEVER`

**Update**: Added pgvector database to persist the SEC documents instead of downloading it everytime. 

---

4. **User Proxy Agent**

**Agent Name**: `User`

**Description**:
- This agent acts as a proxy for the user.
- It does not use a language model.
- It terminates the process when a message contains the keyword "TERMINATE".
- It does not require human input.

**Termination Message Condition**: 
```plaintext
lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"]
```

**Human Input Mode**: `NEVER`

---

These agents work together to automate the process of generating search queries, downloading necessary financial documents, processing these documents, and interacting with the user to provide relevant information. If you need more details or further refinement, let me know!