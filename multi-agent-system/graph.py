from langgraph.graph import StateGraph
from state import TravelState
from agents import planner, researcher, answer_agent

graph = StateGraph(TravelState)

graph.add_node("planner", planner)
graph.add_node("research", researcher)
graph.add_node("answer", answer_agent)

graph.set_entry_point("planner")

graph.add_edge("planner", "research")
graph.add_edge("research", "answer")   # <-- ADD THIS

graph.set_finish_point("answer")

app = graph.compile()