import json
from rank_bm25 import BM25Okapi


with open("data/shl_catalog.json") as f:
    catalog = json.load(f)


documents = []

for item in catalog:

    text = f"""
    {item['name']}
    {item['description']}
    {' '.join(item['skills'])}
    """

    documents.append(text)


tokenized_docs = [
    doc.lower().split()
    for doc in documents
]

bm25 = BM25Okapi(tokenized_docs)


def search_assessments(query, k=5):

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
