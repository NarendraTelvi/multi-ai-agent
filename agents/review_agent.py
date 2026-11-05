from llm import llm


def review_agent(state):

    prompt = f"""
Review the answer for:

1. Accuracy
2. Completeness
3. Hallucinations

Answer:

{state['answer']}
"""

    review = llm.invoke(prompt)

    return {
        "review": review.content
    }