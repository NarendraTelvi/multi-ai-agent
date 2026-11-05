def research_agent(state):

    merged = f"""

DOCUMENT CONTEXT

{state['rag_context']}


WEB CONTEXT

{state['web_context']}

"""

    return {
        "research_context": merged
    }
