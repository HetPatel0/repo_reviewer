from langchain.vectorstores import Chroma

def create_vector_db(docs, embeddings):

    db = Chroma.from_texts(docs, embeddings)

    return db