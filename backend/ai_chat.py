from langchain.chat_models import ChatOpenAI

def chat_with_repo(question, context):

    llm = ChatOpenAI(temperature=0)

    prompt = f"""
    Use the repository context to answer.

    Context:
    {context}

    Question:
    {question}
    """

    return llm.predict(prompt)