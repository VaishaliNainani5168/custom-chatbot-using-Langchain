from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_vector_store(data):
    """Splits text, generates embeddings, and stores in FAISS"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = [item["content"] for item in data]

    if not texts:
        print("No valid text found for embeddings!")
        return None

    split_texts = text_splitter.split_text(" ".join(texts))
    print(f"Total text chunks: {len(split_texts)}")

    # Use a Hugging Face model for embeddings
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_texts(split_texts, embedding_model)

    return vector_db
