from google import genai

client = genai.Client(api_key="AQ.Ab8RN6L9bWM2-KKwXaZoxJk2WnxPZYBEYutLlgahPlUK9yfJmw")

for model in client.models.list():
    print(model.name)

from google import genai

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Hello"
)

print(response.text)