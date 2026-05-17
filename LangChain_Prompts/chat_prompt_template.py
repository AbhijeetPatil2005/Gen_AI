# used for multi turn messages
from langchain_core.prompts import ChatPromptTemplate
from langchian_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful (domain) expert."),
    ('human', "Explain in simple terms what is (topic)")
])

prompt = chat_template.invoke({'domain': 'machine learning', 'topic': 'overfitting'})

print(prompt)