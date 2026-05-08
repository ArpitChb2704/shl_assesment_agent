def refine_query(messages):

    combined = " ".join([
        m["content"]
        for m in messages
        if m["role"] == "user"
    ])

    combined = combined.lower()

    refinement = {
        "personality": False,
        "technical": False,
        "cognitive": False
    }

    if "personality" in combined:
        refinement["personality"] = True

    if "technical" in combined:
        refinement["technical"] = True

    if "cognitive" in combined:
        refinement["cognitive"] = True

    return refinement