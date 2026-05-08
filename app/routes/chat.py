from fastapi import APIRouter

from app.models.schemas import (
    ChatRequest,
    ChatResponse
)

from app.services.conversation import (
    extract_requirements
)

from app.services.guardrails import (
    is_offtopic,
    needs_clarification
)

from app.services.hybrid_search import (
    hybrid_search
)

from app.services.comparison import (
    compare_assessments
)

from app.services.refinement import (
    refine_query
)

from app.services.jd_parser import (
    parse_job_description
)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(req: ChatRequest):

    messages = [
        m.dict()
        for m in req.messages
    ]

    latest_user_message = (
        messages[-1]["content"]
    )

    if is_offtopic(
        latest_user_message
    ):

        return {
            "reply":
            "I can only help with SHL assessments.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "difference" in latest_user_message.lower()
        or
        "compare" in latest_user_message.lower()
    ):

        comparison = compare_assessments(
            latest_user_message
        )

        return {
            "reply": comparison,
            "recommendations": [],
            "end_of_conversation": False
        }

    if len(latest_user_message) > 400:

        jd_data = parse_job_description(
            latest_user_message
        )

        query = " ".join(
            jd_data["skills"]
        )

    else:

        query = latest_user_message

    state = extract_requirements(
        messages
    )

    if needs_clarification(state):

        if not state["skills"]:

            return {
                "reply":
                "What role or technical skills are you hiring for?",
                "recommendations": [],
                "end_of_conversation": False
            }

        if not state["seniority"]:

            return {
                "reply":
                "What seniority level are you hiring for?",
                "recommendations": [],
                "end_of_conversation": False
            }

    refinement = refine_query(
        messages
    )

    if refinement["personality"]:
        query += " personality"

    if refinement["cognitive"]:
        query += " cognitive"

    recommendations = hybrid_search(
        query,
        k=5
    )

    return {
        "reply":
        f"Here are {len(recommendations)} SHL assessments matching your requirements.",
        "recommendations": recommendations,
        "end_of_conversation": True
    }