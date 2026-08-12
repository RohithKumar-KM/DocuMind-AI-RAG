from langchain_community.vectorstores import FAISS

from utils.embeddings import get_embedding_model
from config import VECTOR_DB, TOP_K


def get_retriever():
    """
    Load the FAISS vector database and return a retriever.
    """

    embeddings = get_embedding_model()

    vectorstore = FAISS.load_local(
        VECTOR_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": TOP_K
        }
    )

    return retriever