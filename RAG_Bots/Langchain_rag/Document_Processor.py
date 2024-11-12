import pandas as pd
import numpy as np
from PyPDF2 import *  
from langchain_text_splitters import *
from langchain_experimental.text_splitter import *
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import faiss
import pickle
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


embedding_models = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

import pdfplumber

def pdf_splitter(pdf_doc: str):
    text = ""
    with pdfplumber.open(pdf_doc) as pdf:
        for page in pdf.pages[31:]:  # Adjust start page as needed
            page_text = []
            
            # Extract each word with font size information
            for word in page.extract_words():
                font_size = word.get("height")

                if font_size >= 8:  # Adjust this value as needed
                    page_text.append(word["text"])
                else:
                    pass
                    
            # Join filtered words into a single page text block
            text += " ".join(page_text) + "\n"
    
    return text

# def pdf_splitter(pdf_doc:str):
#     text = ""
#     pdf_obj = PdfReader(pdf_doc)
#     #info = pdf_obj.metadata
#     #number_of_pages = len(pdf_obj.pages)
#     #print(info,number_of_pages)
#     #print(pdf_obj.pages[31:])
#     for pages in pdf_obj.pages[31:]:
#             text += pages.extract_text()
#     return text

def text_chunking_fxn(text):
    method = RecursiveCharacterTextSplitter( separators=["\n\n","\n"],
                                            chunk_size=1000,
                                            chunk_overlap=100,
                                            length_function=len)
    chunks  = method.split_text(text)
    return chunks

def get_vectorstores(text_chunks, vectordb: str):
    if vectordb == 'FAISS':
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embedding_models)
    else:
        vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embedding_models)
    
    return vectorstore


def get_indexing(pdf_name:str,outputfilename:str):
    text = pdf_splitter(pdf_name)
    print("PDF Read and Processed Successfully!!!")
    chunks = text_chunking_fxn(text)
    print("Chunking done of the text Successfully!!!")
    vs = get_vectorstores(chunks,'FAISS')
    print("Stored to vector store successfully!!!")
    # Save the FAISS index to a file
    vs.save_local(outputfilename)
    return vs






