import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils.embeddings import get_embedding_model
import streamlit as st

@st.cache_resource(show_spinner=False)
def build_vectorstore(uploaded_files):

    documents = []

    for file in uploaded_files:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(file.getvalue())

            loader = PyPDFLoader(tmp.name)

            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore