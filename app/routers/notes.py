from fastapi import APIRouter
from fastapi import File, UploadFile
import os
import shutil
from app.services.pdf_service import pdf_reader
from app.services.ai_service import ai_analysis

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)


    # pdf reader
    text = pdf_reader(file_path)

    # ai analysis 
    analysis = ai_analysis(text)

    

    return {
        "file saved" : "File saved successfully",
        "analysis" : analysis
    }


