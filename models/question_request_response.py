from pydantic import BaseModel

class question_asked_request(BaseModel):
  question:str
  
class summarize_title(BaseModel):
  id:str
class get_document(BaseModel):
  id:str
class delete_document(BaseModel):
  id:str
class UploadResponse(BaseModel):
    message: str
    document_id: str
class deletedResponse(BaseModel):
  message:str