from typing import List


def extract_requirements(messages: List[dict]):
    combined = " ".join([
        msg["content"]
        for msg in messages
        if msg["role"] == "user"
    ])

    combined = combined.lower()

    state = {
        "role": None,
        "seniority": None,
        "skills": [],
        "personality": False,
        "cognitive": False,
        "technical": False,
        "stakeholder": False
    }

    if "java" in combined:
        state["skills"].append("java")

    if "python" in combined:
        state["skills"].append("python")

    if "stakeholder" in combined:
        state["stakeholder"] = True

    if "personality" in combined:
        state["personality"] = True

    if "mid" in combined:
        state["seniority"] = "mid"

    if "senior" in combined:
        state["seniority"] = "senior"

    return state