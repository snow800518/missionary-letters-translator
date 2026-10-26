from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import BASE_DIR, UPLOAD_DIR

app = FastAPI(title="Missionary Letters Translator", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "message": "Missionary Letters Translator backend is running"}


@app.post("/api/documents/process")
async def process_document(file: bytes = None, filename: str = "document", source_lang: str = "en", target_lang: str = "ko"):
    from app.services.document_service import DocumentService

    if file is None:
        return {"detail": "File is required"}

    service = DocumentService(UPLOAD_DIR)
    result = await service.process_upload(file=file, filename=filename, source_lang=source_lang, target_lang=target_lang)
    return result


frontend_build = BASE_DIR.parent / "frontend" / "dist"
if frontend_build.exists():
    app.mount("/", StaticFiles(directory=str(frontend_build), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")), reload=True)
