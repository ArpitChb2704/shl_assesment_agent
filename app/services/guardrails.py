OFFTOPIC_KEYWORDS = [
    "salary",
    "legal",
    "visa",
    "tax",
    "politics"
]


def is_offtopic(query: str):
    query = query.lower()

    return any(word in query for word in OFFTOPIC_KEYWORDS)


def needs_clarification(state):
    if not state["skills"]:
        return True

    if not state["seniority"]:
        return True

    return False