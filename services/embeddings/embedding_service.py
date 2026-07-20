from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(self, text: str) -> list[float]:
        return self.model.encode(
            text,
            convert_to_numpy=True
        ).tolist()

    def embed_many(
        self,
        texts: list[str]
    ) -> list[list[float]]:
        return self.model.encode(
            texts,
            convert_to_numpy=True
        ).tolist()