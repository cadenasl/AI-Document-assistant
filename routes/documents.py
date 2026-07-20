from fastapi import APIRouter,UploadFile,File,Depends,HTTPException
from pathlib import Path

import aiofiles
from uuid import uuid4

from services.documents.parser import PDFParserService
from services.documents.chunker import ChunkerService
from models.question_request_response import get_document,delete_document,UploadResponse,deletedResponse
from services.embeddings.vector_store import VectorStore
from services.documents.analyzer import DocumentAnalyzer


router=APIRouter()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
def get_vector_store():
    return VectorStore()

@router.post("/get_document")
async def get_document(data:get_document,vector_store: VectorStore = Depends(get_vector_store)):
 
  results=vector_store.get_document_By_Id(data.id)
  
  return {"document":results}
@router.get("/documents")
async def get_all_documents(vector_store: VectorStore = Depends(get_vector_store)):
  
  return 

@router.post(path="/upload",response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...),vector_store: VectorStore = Depends(get_vector_store),):
    if file.content_type != "application/pdf":
      raise HTTPException(
        status_code=400,
        detail="Only PDF files are allowed."
      )
    file_path = UPLOAD_DIR / file.filename
    document_id = str(uuid4())

    async with aiofiles.open(file_path, "wb") as out_file:
      while chunk := await file.read(1024 * 1024):
        await out_file.write(chunk)

    try:
     result = PDFParserService.extract_text(file_path)
    except Exception as e:
     raise HTTPException(
        status_code=500,
        detail=f"Failed to parse PDF: {e}"
    )
    print(result["pages"])
    chunker = ChunkerService()
    chunks = chunker.chunk_pages(result["pages"])
    
    vector_store.add_document(document_id=document_id,
   
    filename=file.filename,
    chunks=chunks)
    
   
    return UploadResponse(message="The file was uploaded successfully",document_id=document_id)
    
@router.delete("/delete_document",response_model=deletedResponse)
async def delete_document(data:delete_document,vector_store: VectorStore = Depends(get_vector_store)):
  vector_store.delete_document(data.id)
  return deletedResponse(message="document deleted sucessfully")