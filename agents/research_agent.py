from tools.research_tool import search_research
from agents.summarizer_agent import summarize_research

def hayrah_swarm(question):

    papers = search_research(question)

    context = ""

    for p in papers:
        context += f"Title: {p['title']}\nSummary: {p['summary']}\n\n"

    answer = summarize_research(question, context)

    return answer, papers