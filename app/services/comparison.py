from app.services.search import search_assessments


def compare_assessments(query):

    docs = search_assessments(
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
