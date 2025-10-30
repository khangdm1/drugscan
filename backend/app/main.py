# app/main.py
from fastapi import FastAPI
from app.api import drug_api
from app.core.db import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Tạo app FastAPI
app = FastAPI(title="Drug OCR Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép React gọi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Đăng ký route
app.include_router(drug_api.router)

# Tạo bảng nếu chưa có (chỉ dùng dev)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Drug OCR API running!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
