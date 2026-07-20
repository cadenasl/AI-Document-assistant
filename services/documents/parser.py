from pathlib import Path
import fitz


class PDFParserService:
    @staticmethod
    def extract_text(file_path: str | Path):
        document = fitz.open(file_path)

        pages = []

        for page_number, page in enumerate(document, start=1):
            pages.append({
                "page": page_number,
                "text": page.get_text("text").strip()
            })

        return {
            "page_count": len(document),
            "metadata": document.metadata,
            "pages": pages
        }