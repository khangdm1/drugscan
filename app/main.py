# app/main.py
from fastapi import FastAPI
from app.api import drug_api
from app.core.db import engine, Base
# Tạo app FastAPI
app = FastAPI(title="Drug OCR Backend")

# Đăng ký route
app.include_router(drug_api.router)

# Tạo bảng nếu chưa có (chỉ dùng dev)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Drug OCR API running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
