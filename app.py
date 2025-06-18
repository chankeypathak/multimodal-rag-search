import streamlit as st
from src.search import search_knowledge_base

st.set_page_config(page_title="Multimodal RAG Search")
st.title("🔍 Multimodal RAG Search")

query = st.text_input("Enter your query:", "technical diagram of report")

if query:
    with st.spinner("Searching..."):
        results = search_knowledge_base(query)
    st.write("### Top Results")
    for _, row in results.iterrows():
        page_info = f"(Page {row['page']})" if 'page' in row else ""
        st.markdown(f"**Type:** {row['type']}  **Source:** {row['source']} {page_info}")

        if row["type"] == "image":
            st.image(row["content"], width=300)
        else:
            st.text_area("Text", row["text"], height=150)


