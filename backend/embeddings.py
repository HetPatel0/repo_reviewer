from sentence_transformers import SentenceTransformer


def create_embedding_model():

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    return model