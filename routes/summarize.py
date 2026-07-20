from fastapi import APIRouter,UploadFile,File
from pathlib import Path
import shutil

from services.documents.parser import PDFParserService
from services.documents.chunker import ChunkerService
from models.question_request_response import summarize_title
from services.embeddings.vector_store import VectorStore
from services.documents.analyzer import DocumentAnalyzer


router=APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post(path="/summarize")
async def summarize(data:summarize_title):
  vector_database=VectorStore()
  vector_results=vector_database.search(data.id)
  analyze_document=DocumentAnalyzer()
  results=analyze_document.summarize(vector_results)
  return{
        "results":results
    }
