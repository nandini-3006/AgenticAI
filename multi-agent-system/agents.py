from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key="AQ.Ab8RN6L9bWM2-KKwXaZoxJk2WnxPZYBEYutLlgahPlUK9yfJmw"
)

def planner(state):

    prompt=f"""
    Create a travel plan.

    User:

    {state["user_query"]}

    """

    response=llm.invoke(prompt)

    return {

        "plan":response.content

    }

from tools import search_tool

def researcher(state):

    query = state["plan"][0]["text"]

    result = search_tool.invoke(
        {"query": query}
    )

    return {
        "research": str(result)
    }
def answer_agent(state):

    prompt=f"""

    Travel Plan

    {state["plan"]}

    Research

    {state["research"]}

    Create a beautiful itinerary.

    """

    response=llm.invoke(prompt)

    return{

        "answer":response.content

    }