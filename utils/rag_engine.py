from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

from config import OLLAMA_MODEL


class RAGEngine:

    def __init__(self, retriever):

        self.retriever = retriever

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            temperature=0
        )

    def ask(self, question):

        # Retrieve relevant chunks
        docs = self.retriever.invoke(question)

        # Combine retrieved content
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        system_prompt = """
You are DocuMind AI, a helpful document assistant.

Answer the user's question using ONLY the provided document context.

Rules:
- Give the answer directly.
- Do not explain your reasoning.
- Do not mention "the context".
- Do not repeat the question.
- Do not say "the relevant information can be found..."
- Do provide suitable analysis in a few words.
- Do not use information outside the document.
- If the answer is genuinely not available in the document, reply EXACTLY:
"I couldn't find that information in the uploaded document."
- Keep normal answers concise, usually 2-5 sentences.
-give answers inn structured way.
- For summary requests, provide a structured summary with the main points.
"""

        user_prompt = f"""
Document:
--------------------
{context}
--------------------

Question:
{question}

Answer directly:
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        response = self.llm.invoke(messages)

        answer = response.content.strip()

        # Determine whether the answer was found
        not_found_message = (
            "I couldn't find that information in the uploaded document."
        )

        found = answer.lower() != not_found_message.lower()

        return answer, docs, found