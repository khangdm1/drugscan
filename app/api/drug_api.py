# app/api/drug_api.py
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.services import crud
import os

router = APIRouter(prefix="/drugs", tags=["drugs"])

UPLOAD_FOLDER = "uploads"

# GET /drugs?name=paracetamol
@router.get("/", summary="List or search drugs")
def list_drugs(name: str = None, db: Session = Depends(get_db)):
    return crud.get_drugs(db, name=name)

# POST /drugs
@router.post("/", summary="Create new drug")
def create_drug(name: str, db: Session = Depends(get_db)):
    return crud.create_drug(db, name=name)

# POST /drugs/upload
@router.post("/upload", summary="Upload image (placeholder for ML)")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    log = crud.create_prediction_log(db, predicted_drug_id=None, confidence=None, image_path=file_path)
    return {"status": "ok", "log_id": log.id, "path": file_path}
