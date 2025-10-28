# app/services/crud.py
from sqlalchemy.orm import Session
from app.models.drug import Drug
from app.models.prediction_log import PredictionLog

# Lấy danh sách hoặc tìm kiếm theo tên
def get_drugs(db: Session, skip: int = 0, limit: int = 100, name: str = None):
    q = db.query(Drug)
    if name:
        q = q.filter(Drug.name.ilike(f"%{name}%"))
    return q.offset(skip).limit(limit).all()

# Tạo mới một thuốc
def create_drug(db: Session, name: str, **kwargs):
    drug = Drug(name=name, **kwargs)
    db.add(drug)
    db.commit()
    db.refresh(drug)
    return drug

# Ghi log khi người dùng upload ảnh (chưa có ML)
def create_prediction_log(db: Session, predicted_drug_id: int = None, confidence: float = None, image_path: str = None):
    log = PredictionLog(predicted_drug_id=predicted_drug_id, confidence=confidence, image_path=image_path)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
