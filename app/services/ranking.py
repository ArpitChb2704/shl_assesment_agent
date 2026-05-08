from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5" 
)

vectorstore = FAISS.load_local(
    "data/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def retrieve_assessments(query: str, k=10):
    docs = vectorstore.similarity_search(query, k=k)

    recommendations = []

    for doc in docs:
        recommendations.append({
            "name": doc.metadata["name"],
            "url": doc.metadata["url"],
            "test_type": doc.metadata["test_type"]
        })

    return recommendations
