from langchain_community.document_loaders import csv_loader
loader = csv_loader.CSVLoader('sample.csv')
docs = loader.load()
print(len(docs))