from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

template = """
Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Use PromptTemplate correctly
prompt = PromptTemplate.from_template(template)

# Load the Ollama model
model = OllamaLLM(model="llama3")

# Create a chain
chain = prompt | model

# Function to handle conversation
def handle_conversation():
    context = ""
    print("Welcome to DebAI! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("DebAI: Goodbye!")
            break

        # Check if the user asks for the chatbot's name
        if "your name" in user_input.lower() or "who are you" in user_input.lower():
            bot_response = "My name is DebAI, your personal AI assistant!"
        else:
            # Invoke the model if it's a normal question
            result = chain.invoke({"context": context, "question": user_input})
            bot_response = result.content if hasattr(result, "content") else str(result)

        print("DebAI:", bot_response)

        # Append conversation history
        context += f"\nUser: {user_input}\nDebAI: {bot_response}" 

if __name__ == "__main__":
    handle_conversation()
