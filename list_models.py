from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JKnY028M7J1ELE0Sya8y8lRgoVJWYn5-o4JsGCq1NlEA")

for model in client.models.list():
    print(model.name)