from typing import TypedDict


class AgentState(TypedDict):
    query: str

    rag_context: str
    web_context: str
    research_context: str

    answer: str
    review: str

    final_report: str