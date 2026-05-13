from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

documents =[
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Bangalore is the IT hub of India."
]
result = embedding.embed_documents(documents)

for i, doc in enumerate(documents):
    print(f"Document {i+1}: {doc}")
    print(f"Embedding: {str(result[i])}")
