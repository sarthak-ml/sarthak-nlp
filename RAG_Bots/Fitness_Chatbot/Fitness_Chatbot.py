from langchain_ollama import OllamaLLM
from Chatbot_Class import Chatstate

model = OllamaLLM(model = "gemma2:2b")

chat = Chatstate(model)

# Start the continuous chat loop
while True:
    print("Type exit, quit, end or stop to end the chat.")
    message = input("You: ")  # Get user input

    if message.lower() in ["exit", "quit", "stop", "end"]:  # Check for end condition
        print("Chat ended. Adios amigo it was nice talking to you.")
        break  # Exit the loop if user wants to end the chat
    
    output = chat.output(message)  # Get the chatbot's response
    print(f"Bot: {output}")  # Display the response

