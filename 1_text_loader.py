from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

prompt = PromptTemplate(
    input_variables=["text"],
    template="Extract the summary of the following text: {text}"
)

output_parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()


print(type(docs), len(docs))

print(type(docs[0]))
# print(docs[0])

# to extract only the content of the document
# print(docs[0].page_content)

# to extract only the metadata of the document
print(docs[0].metadata)

chain = prompt | model | output_parser

print(chain.invoke({'text': docs[0].page_content}))