from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load PDF
loader = PyPDFLoader("document.pdf")
documents = loader.load()

print("PDF Loaded")

# Split PDF into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print("Chunks Created:", len(chunks))

# Create embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)

# Save database
vector_db.save_local("vectorstore")

print("Vector Database Saved")