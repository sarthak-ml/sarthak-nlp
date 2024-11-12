import Document_Processor as DP
from langchain.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings('ignore')


embedding_models = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
#vector_store = DP.get_indexing('coi.pdf','coi_faiss')  uncomment this only when u want to create new vectorstor
vectorstore = FAISS.load_local("coi_faiss",embeddings=embedding_models,allow_dangerous_deserialization=True) #this is for reloading the vector store created


def create_conversation(vectorstore,model_name:str, model_temperature):
    llm = OllamaLLM(model=model_name)
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm = llm,retriever = vectorstore.as_retriever(),memory=memory)
    return conversation_chain

def run_conversation(conversation_chain, user_input: str):
    response = conversation_chain({"question": user_input})
    return response['answer']

def chat_until_bye(conversation_chain):
    print("Bot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")  
        if "okay bye" in user_input.lower():  
            print("Bot: Goodbye! Have a great day!")
            break  # Exit the loop if user says 'okay bye'
        
        # Otherwise, continue conversation
        bot_response = run_conversation(conversation_chain, user_input)
        print("Bot:", bot_response)

conversation = create_conversation(vectorstore, model_name='gemma2:2b', model_temperature=0.7)
chat_until_bye(conversation)


