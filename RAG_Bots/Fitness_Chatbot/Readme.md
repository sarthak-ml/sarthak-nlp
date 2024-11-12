**This repository provides a Python script for a conversational AI bot tailored to assist users on their fitness journey. The bot answers questions related to fitness and can provide food recommendations or workout plans based on user preferences. It uses a structured conversation history to maintain context throughout the interaction.**


**Introduction**

This AI chatbot is designed specifically for fitness-related conversations. It has a unique tone for handling irrelevant questions with humor and can provide helpful advice on workout routines and meal plans based on user information. The bot follows a specific structure to ensure the conversation remains focused and useful.

**Features**
**Contextual Fitness Advice**: The bot provides answers about fitness, including meal plans and workouts, based on user inputs.
**Personalized Conversations**: Takes user information such as name, age, food preferences, and allergies into account.
**Structured Responses:** Tracks and structures conversation history for better context awareness.
Humorous Handling of Off-topic Questions: Responds humorously to questions outside the fitness domain.

**Requirements**
Python 3.9 or later
Required packages: langchain_ollama

***Explanation of Key Classes and Functions***

***Chatstate Class***
This class manages the chatbot’s conversation state, handling user input, generating responses, and managing the structured conversation history.

**Attributes:**
__st_user_token__, __end_user_token__: Tokens marking the start and end of a user’s message.
__st_bot_token__, __end_bot_token__: Tokens marking the start and end of the bot’s response.
history: List containing all conversation messages (system prompt, user, and bot).
system: Defines the bot's guiding principles and response rules.
Methods:

__init__: Initializes the bot with the specified model and system prompt.
add_history_of_user: Adds a user's message to the conversation history.
add_history_of_bot: Adds the bot’s response to the conversation history.
get_chat_history: Returns the entire chat history as a formatted string.
get_prompt: Combines the chat history and system prompt to form the final prompt for the model.
output: Generates the bot's response, adds it to history, and returns it.

**Chat Loop**
The loop interacts continuously with the user until an exit command is given. User input is processed by the Chatstate instance, and the bot’s response is printed.


