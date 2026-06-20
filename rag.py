import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Gemini API Key
genai.configure(
    api_key="AQ.Ab8RN6LtemdaZbAvvLm7hkllwYtfedaWSoeeAXwH2RQjmmLSKg"
)

# Gemini Model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Vector Database
vector_db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

def get_answer(question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = ""

    for doc in docs:
        context += doc.page_content + "\n"

    prompt = f"""
You are a Question Answering assistant.

Answer only from the provided context.

If answer is not available,
return exactly:

The answer is not available in the provided document.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text