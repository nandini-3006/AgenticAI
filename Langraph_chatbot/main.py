from typing import Optional
from xml.parsers.expat import model
from google import genai
from langgraph.graph import StateGraph
from typing_extensions import TypedDict

  
class GraphState(TypedDict):
    question: Optional[str]
    classification: Optional[str]
    response: Optional[str]

client = genai.Client(api_key="AQ.Ab8RN6JKnY028M7J1ELE0Sya8y8lRgoVJWYn5-o4JsGCq1NlEA")
def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
             model="gemini-3.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("ERROR:", e)
        return "Sorry, something went wrong."

def classify(state: GraphState) -> GraphState:
    question = state.get("question", "").lower()

    if any(word in question for word in ["hello", "hi", "hey"]):
        classification = "greeting"
    else:
        classification = "search"

    return {
        **state,
        "classification": classification
    }

def respond(state: GraphState) -> GraphState:
    classification = state.get("classification")
    question = state.get("question")

    if classification == "greeting":
        response = "Hello! How can I help you today?"

    elif classification == "search":
        response = ask_gemini(question)

    else:
        response = "I don't know how to respond."

    return {
        **state,
        "response": response
    }

builder = StateGraph(GraphState)

builder.add_node("classify", classify)
builder.add_node("respond", respond)

builder.set_entry_point("classify")

builder.add_edge("classify", "respond")

builder.set_finish_point("respond")

app = builder.compile()

print("=== LangGraph Chatbot ===")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    result = app.invoke({
        "question": user_input
    })

    print("Bot:", result["response"])


