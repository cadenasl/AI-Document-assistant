from fastapi import FastAPI
from routes.ask import router as ask_router
from routes.summarize import router as summarize_router
from routes.documents import router as document_router



app = FastAPI()
app.include_router(ask_router)
app.include_router(summarize_router)
app.include_router(document_router)



