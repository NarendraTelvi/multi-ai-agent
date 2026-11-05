from llm import llm


def coding_agent(state):

    prompt = f"""
You are an expert AI Engineer.

Use all the information
available below.

{state['research_context']}

Question:
{state['query']}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }