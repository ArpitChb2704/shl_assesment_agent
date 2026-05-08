import re


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalize_query(query):

    return query.lower().strip()


def deduplicate_recommendations(recommendations):

    seen = set()
    unique = []

    for item in recommendations:

        if item["name"] not in seen:

            seen.add(item["name"])
            unique.append(item)

    return unique