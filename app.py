import tempfile
import streamlit as st

from rag import ingest_pdf
from graph import graph

st.set_page_config(
    page_title="Multi-Agent System",
    layout="wide"
)

st.title(
    "🤖 LangGraph Multi-Agent System"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(
            uploaded_file.read()
        )

        temp_path = tmp.name

    with st.spinner(
        "Processing PDF..."
    ):
        ingest_pdf(temp_path)

    st.success(
        "PDF Indexed Successfully"
    )

query = st.text_area(
    "Ask a question"
)

if st.button(
    "Run Agents"
):

    if not query:
        st.warning(
            "Please enter a question"
        )

    else:

        with st.spinner(
            "Running Agents..."
        ):

            result = graph.invoke(
                {
                    "query": query
                }
            )

        st.markdown(
            result["final_report"]
        )
