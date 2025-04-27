import streamlit as st, os, pathlib, json
from langgraph import Graph
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

DATA_DIR = pathlib.Path("data")

def load_db(project):
    return Chroma(persist_directory=str(DATA_DIR / project),
                  embedding_function=OpenAIEmbeddings())

def query_specs(question, project):
    db = load_db(project)
    docs = db.similarity_search(question, k=6)
    context = "\n\n".join([d.page_content for d in docs])
    prompt = f"{context}\n\nQ: {question}\nA:"
    answer = OpenAI().invoke(prompt)
    cites = [{"page": d.metadata.get("page", "?"), "snippet": d.page_content[:80]}
             for d in docs]
    return {"answer": answer, "citations": cites}

st.title("Spec-Bot")
mode = st.radio("Mode", ("Upload PDF", "Use stored project"))

if mode == "Upload PDF":
    pdf = st.file_uploader("PDF spec")
    project = st.text_input("Project name")
    if pdf and project and st.button("Ingest"):
        tmp = pathlib.Path("docs") / pdf.name
        tmp.write_bytes(pdf.getvalue())
        os.system(f"python scripts/ingest_pdf.py {tmp} --project {project}")
        st.success("Ingested!")

else:
    project = st.selectbox("Project", sorted(p.name for p in DATA_DIR.iterdir()))

q = st.text_area("Ask a question")
if st.button("Answer") and q and project:
    with st.spinner("Thinking…"):
        res = query_specs(q, project)
    st.markdown(res["answer"])
    for c in res["citations"]:
        st.markdown(f"- p.{c['page']}: *{c['snippet']}…*") 