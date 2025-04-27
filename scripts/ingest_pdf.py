#!/usr/bin/env python3
"""
Ingest a PDF spec → split → embed → store in Chroma.
Usage: python scripts/ingest_pdf.py <pdf_path> --project <name>
"""
import argparse, pathlib, os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings   # swap if local

def main(pdf_path: str, project: str):
    docs_dir = pathlib.Path("data") / project
    docs_dir.mkdir(parents=True, exist_ok=True)

    pages = PyPDFLoader(pdf_path).load()          # one doc per page
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900, chunk_overlap=100, separators=["\n", " "])
    chunks = splitter.split_documents(pages)

    db = Chroma(persist_directory=str(docs_dir),
                embedding_function=OpenAIEmbeddings())
    db.add_documents(chunks)
    db.persist()
    print(f"✅ Stored {len(chunks)} chunks → {docs_dir}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf_path"), ap.add_argument("--project", required=True)
    main(**vars(ap.parse_args())) 