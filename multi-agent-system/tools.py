from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(
    max_results=5,
    tavily_api_key="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"
)