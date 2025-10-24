from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('indian_economy_report_2025.pdf')

docs = loader.load()

print(type(docs), len(docs))

print(docs[0].page_content)
print(docs[0].metadata)