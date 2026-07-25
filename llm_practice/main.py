import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "I love AI"

tokens = enc.encode(text)

print(tokens)

def count_tokens(text):
    return len(enc.encode(text))

text = open('document.txt', 'r', encoding='utf-8').read()

print('Total tokens:', count_tokens(text))

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embedding = model.encode("I love programming")

print(len(embedding))
print(embedding[:5])

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

v1 = np.array([[1, 1]])
v2 = np.array([[2, 2]])
v3 = np.array([[1, 0]])

print(cosine_similarity(v1, v2))  # ~1.0
print(cosine_similarity(v1, v3))  # ~0.7


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    'How to install Python',
    'Java collections tutorial',
    'Best pizza in Mumbai'
]

query = 'Python installation guide'

vectorizer = TfidfVectorizer()

doc_vectors = vectorizer.fit_transform(docs)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, doc_vectors)

print(scores)

import torch

Q = torch.tensor([[1,0]])
K = torch.tensor([[1,0]])

V = torch.tensor([[5,10]])

score = Q @ K.T
print("Query and key similarity score:")
print(score)
from google import genai
from pydantic import BaseModel
import json

client = genai.Client(api_key="AQ.Ab8RN6JKnY028M7J1ELE0Sya8y8lRgoVJWYn5-o4JsGCq1NlEA")

class User(BaseModel):
    name: str
    age: int

response = client.models.generate_content(
    model="gemini-3.5-flash",   # your working model
    contents="""
Extract the user details and return ONLY valid JSON.

Text:
Rahul is 22 years old

Format:
{
  "name": "",
  "age": 0
}
"""
)

print(response.text)

data = json.loads(response.text)
user = User(**data)

print(user)

