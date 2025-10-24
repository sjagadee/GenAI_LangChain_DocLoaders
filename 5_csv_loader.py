from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('Social_Network_Ads.csv')

# also can use lazy load functions
docs = loader.load()

print(type(docs), len(docs))

print(docs[0].page_content)
print(docs[0].metadata)