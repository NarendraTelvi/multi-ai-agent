from langgraph.graph import StateGraph
from langgraph.graph import END

from state import AgentState

from agents.rag_agent import rag_agent
from agents.web_agent import web_agent
from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.review_agent import review_agent
from agents.reporting_agent import reporting_agent

builder = StateGraph(
    AgentState
)

builder.add_node(
    "rag",
    rag_agent
)

builder.add_node(
    "web",
    web_agent
)

builder.add_node(
    "research",
    research_agent
)

builder.add_node(
    "coding",
    coding_agent
)

builder.add_node(
    "review",
    review_agent
)

builder.add_node(
    "reporting",
    reporting_agent
)

builder.set_entry_point(
    "rag"
)

builder.add_edge(
    "rag",
    "web"
)

builder.add_edge(
    "web",
    "research"
)

builder.add_edge(
    "research",
    "coding"
)

builder.add_edge(
    "coding",
    "review"
)

builder.add_edge(
    "review",
    "reporting"
)

builder.add_edge(
    "reporting",
    END
)

graph = builder.compile()