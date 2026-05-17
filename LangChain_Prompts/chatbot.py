from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if(user_input=='exit'):
        print("Exiting the chatbot. Goodbye!")
        break
    
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print('Chatbot:', response.content)
    
print(chat_history)    