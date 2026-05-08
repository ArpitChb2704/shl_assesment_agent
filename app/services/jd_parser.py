import os
import json

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.prompts import (
    ChatPromptTemplate
)


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    ),
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    """
    Extract hiring requirements from this JD.

    Return JSON only.

    Required keys:
    - skills
    - seniority
    - personality
    - communication
    - leadership

    JD:
    {jd}
    """
)


def parse_job_description(jd):

    chain = prompt | llm

    response = chain.invoke({
        "jd": jd
    })

    return json.loads(
        response.content
    )