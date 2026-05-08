import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL
)

with open("data/shl_catalog.json") as f:
    catalog = json.load(f)


def build_vectorstore():
    docs = []

    for item in catalog:
        text = f"""
        Name: {item['name']}
        Description: {item['description']}
        Skills: {item['skills']}
        Test Type: {item['test_type']}
        """

        docs.append(
            Document(
                page_content=text,
                metadata={
                    "name": item["name"],
                    "url": item["url"],
                    "test_type": item["test_type"]
                }
            )
        )

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("data/faiss_index")


if __name__ == "__main__":
    build_vectorstore()