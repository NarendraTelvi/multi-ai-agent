from duckduckgo_search import DDGS


def web_agent(state):

    query = state["query"]

    outputs = []

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=5
            )

            for r in results:
                outputs.append(
                    r["body"]
                )

    except Exception as e:

        outputs.append(
            str(e)
        )

    return {
        "web_context": "\n".join(outputs)
    }