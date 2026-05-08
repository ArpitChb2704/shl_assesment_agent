from app.services.hybrid_search import hybrid_search


def compare_assessments(query):

    docs = hybrid_search(
        query,
        k=2
    )

    if len(docs) < 2:

        return (
            "Unable to compare "
            "the requested assessments."
        )

    first = docs[0]
    second = docs[1]

    comparison = f"""
    {first['name']}
    focuses on:
    {first['description']}

    {second['name']}
    focuses on:
    {second['description']}
    """

    return comparison