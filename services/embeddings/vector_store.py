import chromadb

from services.embeddings.embedding_service import (
    EmbeddingService,
)


class VectorStore:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_document(
        self,
        document_id: str,
        filename: str,
        chunks: list[dict],
    ):
        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.embedding_service.embed_many(
            texts
        )

        ids = [
            f"{document_id}_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
    {
        "document_id": document_id,
        "filename": filename,
        "page": chunk["page"],
        "chunk_index": i,
    }
    for i, chunk in enumerate(chunks)
]

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        return len(chunks)

    def search(
        self,
        query: str,
        limit: int = 5,
    ):

        embedding = self.embedding_service.embed(
            query
        )

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=limit,
        )

        return results["documents"][0]
    def get_document_By_Id( self,
        document_id: str,):
        document = self.collection.get(where={
            "document_id": document_id
        })
        return document
        
    def delete_document(
        self,
        document_id: str,
    ):

        self.collection.delete(
            where={
                "document_id": document_id
            }
        )
    def debug(self):
     print(self.collection.get())
    def get_all_documents(self):
      results = self.collection.get(include=["metadatas"])

      documents = {}

      for metadata in results["metadatas"]:
        doc_id = metadata["document_id"]

        if doc_id not in documents:
            documents[doc_id] = {
                "document_id": doc_id,
                "filename": metadata["filename"],
            }

      return list(documents.values())