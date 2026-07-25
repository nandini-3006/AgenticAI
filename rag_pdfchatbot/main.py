from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("test_pdf.pdf")

documents = loader.load()
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

from langchain_google_genai import GoogleGenerativeAIEmbeddings
API_KEY = "AQ.Ab8RN6L9bWM2-KKwXaZoxJk2WnxPZYBEYutLlgahPlUK9yfJmw"
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=API_KEY
)

from langchain_community.vectorstores import FAISS

db = FAISS.from_documents(
    chunks,
    embeddings
)

question = input("Ask: ")

docs = db.similarity_search(
    question,
    k=3
)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=API_KEY
)

context = "\n".join(doc.page_content for doc in docs)

response = llm.invoke(
    f"""
Context:

{context}

Question:

{question}
"""
)

print(response.content[0]["text"])