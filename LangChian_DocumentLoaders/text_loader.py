from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
prompt = PromptTemplate(
    template='Write a summary for the following {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt',encoding='utf-8')

documents = loader.load()
print(documents)
print(type(documents))
print(documents[0].page_content)
print(documents[0].metadata)

chain = prompt | model | parser 
print(chain.invoke({'poem':documents[0].page_content}))