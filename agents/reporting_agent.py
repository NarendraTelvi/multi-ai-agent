def reporting_agent(state):

    final = f"""
## Answer

{state['answer']}

---

## Review

{state['review']}
"""

    return {
        "final_report": final
    }