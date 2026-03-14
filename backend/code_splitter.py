from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_code(code_files):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = []

    for file in code_files:

        chunks = splitter.split_text(file["content"])

        for chunk in chunks:
            docs.append({
                "path": file["path"],
                "content": chunk
            })

    return docs