import arxiv

def search_research(query):

    results = arxiv.Search(
        query=query,
        max_results=5
    )

    papers = []

    for r in results.results():
        papers.append({
            "title": r.title,
            "summary": r.summary
        })

    return papers