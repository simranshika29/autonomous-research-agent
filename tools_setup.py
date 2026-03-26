from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
import wikipedia

search = DuckDuckGoSearchRun()

web_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Search latest information from web"
)

def wiki_search(query):
    return wikipedia.summary(query, sentences=5)

wiki_tool = Tool(
    name="Wikipedia",
    func=wiki_search,
    description="Get information from Wikipedia"
)

tools = [web_tool, wiki_tool]