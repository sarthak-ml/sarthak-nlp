**Introduction**

The code is designed to load a PDF document, process it by splitting the text into chunks, store these chunks in a vector store (FAISS), and then utilize LangChain's conversational tools to create an interactive chatbot. The chatbot can answer questions based on the document's content until the user exits by saying "okay bye."

**Features**

PDF Document Parsing: Extracts text from a PDF, filters it based on font size, and processes it into chunks for indexing.
Vector Storage with FAISS: Uses FAISS to store and retrieve text chunks for quick, efficient responses.
Conversational AI: Incorporates LangChain’s conversational tools and memory for coherent, context-aware interactions.
Configurable LLM: Utilizes Ollama's LLM for language generation, adjustable with model parameters.

**Requirements**
Python 3.9 or later
Packages: PyPDF2, pdfplumber, faiss, langchain, langchain_community, pickle, pandas, numpy
Access to Ollama's LLM


**Explanation of Key Functions**


pdf_splitter(pdf_doc: str): Extracts text from each page of a PDF, filtering out smaller fonts to focus on main content.

text_chunking_fxn(text): Splits the extracted text into manageable chunks with specified overlap, optimizing it for vector storage.

get_vectorstores(text_chunks, vectordb: str): Creates a vector store using FAISS or Chroma for the given text chunks. The vector store enables efficient retrieval of chunks during conversation.

get_indexing(pdf_name: str, outputfilename: str): Integrates pdf_splitter, text_chunking_fxn, and get_vectorstores functions to process a PDF and save it into a FAISS vector store file.

create_conversation(vectorstore, model_name: str, model_temperature): Configures the conversational chain using LangChain, embedding the LLM and memory to maintain context.

run_conversation(conversation_chain, user_input: str): Runs a single round of question-and-answer within the conversation chain.
chat_until_bye(conversation_chain): Loops the chatbot interaction until the user inputs "okay bye".
