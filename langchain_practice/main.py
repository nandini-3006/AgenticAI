from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key = "AQ.Ab8RN6JKnY028M7J1ELE0Sya8y8lRgoVJWYn5-o4JsGCq1NlEA"

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7,
    google_api_key=api_key
)

template = "Give me 3 skills that are in demand in {year}."

prompt = PromptTemplate.from_template(template)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({"year": "2026"})

print(response)