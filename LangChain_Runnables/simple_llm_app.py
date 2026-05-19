from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# . Initialize the LLM
model = ChatGroq(model ="llama-3.3-70b-versatile")

# . Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# . Define the input
topic = input('Enter a topic')

# . Format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

# . Call the LLM directly
blog_title = model.predict(formatted_prompt)

# . Print the output
print("Generated Blog Title:", blog_title)