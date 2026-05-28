from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample_doc.pdf')

docs = loader.load()

print(len(docs))