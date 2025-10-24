from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

prompt = PromptTemplate(
    input_variables=["text", "question"],
    template="Answer the following {question} based on the given text: {text}"
)

output_parser = StrOutputParser()

loader = WebBaseLoader('https://en.wikipedia.org/wiki/Belgaum')

docs = loader.load()

chain = prompt | model | output_parser

print(chain.invoke({'text': docs[0].page_content, 'question': 'What percentage of people speak in Kannada in Belgaum?'}))