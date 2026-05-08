from app.services.bm25 import bm25_search
from app.services.ranking import retrieve_assessments


def hybrid_search(query, k=10):

    semantic_results = retrieve_assessments(
        query,
        k=k
    )

    keyword_results = bm25_search(
        query,
        k=k
    )

    combined = []

    seen = set()

    for item in semantic_results + keyword_results:

        name = item["name"]

        if name not in seen:

            seen.add(name)

            combined.append(item)

    return combined[:k]