from fastapi import APIRouter,UploadFile,File
from pathlib import Path
import shutil

from services.documents.parser import PDFParserService
from services.documents.chunker import ChunkerService
from models.question_request_response import question_asked_request
from services.embeddings.vector_store import VectorStore
from services.documents.analyzer import DocumentAnalyzer


router=APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post(path="/ask")
async def ask_question(data:question_asked_request):
    vector_database=VectorStore()
    vector_results=vector_database.search(data.question)
    analyze_document=DocumentAnalyzer()
    results=analyze_document.answer_question(data.question,vector_results)
    return{
        "results":results
    }

