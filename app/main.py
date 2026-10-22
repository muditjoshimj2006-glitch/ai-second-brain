from fastapi import FastAPI
from app.routers.notes import router as note_router

app = FastAPI(
    title="AI Second Brain API",
    description="AI Powered Personal Knowledge Management System",
    version="1.0.0"
    )

app.include_router(note_router)


@app.get("/")
def root():
    return{
        "message" : "Welcome To The AI Second Brain"
    }