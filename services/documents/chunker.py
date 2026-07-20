from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkerService:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )

    def chunk_pages(self, pages: list[dict]):
          chunks = []

          for page in pages:
            page_chunks = self.splitter.split_text(page["text"])

            for i, chunk in enumerate(page_chunks):
                chunks.append({
                    "page": page["page"],
                    "chunk_index": i,
                    "text": chunk
                })

          return chunks