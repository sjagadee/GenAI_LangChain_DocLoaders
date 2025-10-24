from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader 
)

#  loads all the data at once and then start processing
# docs = loader.load()

# load data one by one
docs = loader.lazy_load()
# lazy load gives a generator object - that means it will load data one by one in memory.

# print(type(docs), len(docs))

# print(docs[350].page_content)
# print(docs[350].metadata)

for document in docs:
    print(document.metadata)