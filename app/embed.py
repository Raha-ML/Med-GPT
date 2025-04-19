from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma 

def embed_and_store(chuncks, persist_dir='db') :
    embeding_model = 'sentence-transformers/all-MiniLM-L6-v2'
    embedder = HuggingFaceEmbeddings(model_name=embeding_model)

    vector_db  = Chroma.from_documents(chuncks, embedder, persist_directory=persist_dir)
    vector_db.persist()
    return vector_db

