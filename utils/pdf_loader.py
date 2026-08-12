from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(folder_path: str):
    """
    Load every PDF inside the folder.
    """

    documents = []

    pdf_files = Path(folder_path).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents