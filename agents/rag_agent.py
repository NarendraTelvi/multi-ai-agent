from rag import retrieve


def rag_agent(state):

    query = state["query"]

    context = retrieve(query)

    return {
        "rag_context": context
    }