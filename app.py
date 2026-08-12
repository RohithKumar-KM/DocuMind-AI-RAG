import streamlit as st

from utils.vectorstore import build_vectorstore
from utils.rag_engine import RAGEngine
# PAGE CONFIG
st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# CUSTOM CSS
st.markdown("""
<style>
.stApp,.main{background:#fff!important}
.block-container{max-width:1100px;padding:2rem 0 4rem}

.documind-header{text-align:center;padding:.5rem 0 2rem}
.documind-title{font-size:2.5rem;font-weight:750;color:#102a43!important}
.documind-subtitle{font-size:1rem;color:#52606d!important}

section[data-testid="stSidebar"],
section[data-testid="stSidebar"]>div{
    background:#8db0f2!important
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label{
    color:#0d1a33!important
}
section[data-testid="stSidebar"] hr{
    border-color:rgba(13,26,51,.2)!important
}

.sidebar-brand{text-align:center;padding:.5rem 0 1.2rem}
.sidebar-icon{font-size:2.3rem}
.sidebar-title{font-size:1.3rem;font-weight:700;color:#0d1a33!important}
.sidebar-description{font-size:.82rem;color:#243b5a!important}

[data-testid="stFileUploader"]{
    background:#bfd3f5!important;
    border:2px dashed #5f83c4!important;
    border-radius:12px!important;
    padding:.6rem!important
}
[data-testid="stFileUploaderDropzone"]{
    background:#f7faff!important;
    border-radius:9px!important
}
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] small{
    color:#0d1a33!important;
    opacity:1!important
}
[data-testid="stFileUploaderDropzone"] button,
.stButton>button{
    background:#147d92!important;
    color:#fff!important;
    border:0!important;
    border-radius:8px!important;
    font-weight:600!important
}
[data-testid="stFileUploaderDropzone"] button:hover,
.stButton>button:hover{
    background:#0f6678!important
}
[data-testid="stFileUploaderFileName"]{
    color:#0d1a33!important;
    font-weight:600!important
}

[data-testid="stChatMessage"]{
    border-radius:12px!important;
    margin-bottom:.8rem!important;
    padding:.8rem 1rem!important
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]){
    background:#eef6f8!important;
    border:1px solid #cce4e9!important
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]){
    background:#f7f9fb!important;
    border:1px solid #d9e2ec!important
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li{
    color:#172033!important;
    line-height:1.6!important
}

[data-testid="stChatInput"]>div{
    background:#fff!important;
    border:1px solid #9fb3c8!important;
    border-radius:12px!important
}
[data-testid="stChatInput"] textarea{
    color:#172033!important;
    -webkit-text-fill-color:#172033!important
}
[data-testid="stChatInput"] textarea::placeholder{
    color:#6b7280!important;
    opacity:1!important
}

[data-testid="stExpander"]{
    background:#f8fafc!important;
    border:1px solid #d9e2ec!important;
    border-radius:9px!important
}
[data-testid="stExpander"] p,
[data-testid="stExpander"] span{
    color:#243b53!important
}

.footer{
    width:100vw!important;
    margin:2rem 0 1rem calc(-50vw + 50%)!important;
    text-align:center!important;
    color:#64748b!important;
    font-size:1rem!important
}
</style>
""", unsafe_allow_html=True)
# HEADER
st.markdown(
    """
<div class="documind-header">
    <div class="documind-title">🧠 DocuMind AI</div>
    <div class="documind-subtitle">
        Intelligent document analysis powered by Ollama
    </div>
</div>
""",
    unsafe_allow_html=True
)
# SIDEBAR
with st.sidebar:
    st.markdown(
        """
<div class="sidebar-brand">
    <div class="sidebar-icon">📚</div>
    <div class="sidebar-title">DocuMind AI</div>
    <div class="sidebar-description">
        Your one stop document assistant
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    st.divider()
    st.markdown("### 📂 Documents")
    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type="pdf",
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown(
        """
<div class="sidebar-description">
<b>How it works</b><br><br>

1. Upload your PDF<br>
2. DocuMind indexes the document<br>
3. Ask questions about it<br>
4. Answers are generated using Ollama
</div>
""",
        unsafe_allow_html=True
    )
# DOCUMENT PROCESSING
if uploaded_files:
    if "bot" not in st.session_state:
        with st.spinner("Reading and indexing your document..."):
            st.session_state.vectorstore = build_vectorstore(
                uploaded_files
            )
            retriever = st.session_state.vectorstore.as_retriever(
                search_kwargs={"k": 4}
            )
            st.session_state.bot = RAGEngine(retriever)
        st.success("Documents are ready Exploration.")
# CHAT
    question = st.chat_input(
        "Ask something about your document..."
    )
    if question:
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("AI"):
            with st.spinner("Thinking..."):
                answer, docs, found = st.session_state.bot.ask(
                    question
                )
            st.write(answer)
            # Only show sources if answer was found
            if found:

                with st.expander("📚 Sources relevant your searches"):

                    seen_pages = set()

                    for doc in docs:

                        page = doc.metadata.get(
                            "page",
                            0
                        ) + 1

                        key = page

                        if key not in seen_pages:

                            seen_pages.add(key)

                            st.write(
                                f"📄 Page {page}"
                            )
# EMPTY STATE
else:

    st.markdown(
        """
    <div style="
    text-align: center;
    margin-top: 4rem;
    padding: 2.5rem;
    background-color: #f7f9fb;
    border: 1px solid #e1e7ed;
    border-radius: 14px;">

    <div style="font-size: 3rem;">📄</div>

    <h2 style="
        color: #102a43;
        margin-bottom: 0.5rem;
    ">
        Upload a document to get started
    </h2>

    <p style="
        color: #52606d;
        font-size: 1rem;
    ">
        Ask questions and explore your documents using DocuMind AI.
    </p>

    </div>
""",
        unsafe_allow_html=True
    )
# FOOTER
st.markdown(
    """
<div class="footer">
    DocuMind AI • Powered by LangChain, FAISS & Ollama<br>
    <b>Developed by Rohith Kumar K M</b>
</div>
""",
    unsafe_allow_html=True
)