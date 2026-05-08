import json
from rank_bm25 import BM25Okapi


with open("data/shl_catalog.json") as f:
    catalog = json.load(f)


documents = [
    item["description"]
    for item in catalog
]


tokenized_docs = [
    doc.lower().split()
    for doc in documents
]

bm25 = BM25Okapi(tokenized_docs)


def bm25_search(query, k=10):

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        zip(scores, catalog),
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        item
        for score, item in ranked[:k]
    ]