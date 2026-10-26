from __future__ import annotations

from pathlib import Path

from app.services.ocr_service import OCRService
from app.services.translation_service import TranslationService


class DocumentService:
    def __init__(self, upload_dir: Path) -> None:
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def process_upload(self, file: bytes, filename: str, source_lang: str, target_lang: str) -> dict:
        safe_name = Path(filename).name
        target_path = self.upload_dir / safe_name

        with open(target_path, "wb") as handle:
            handle.write(file)

        ocr_text = OCRService.extract_text(target_path)
        translated = TranslationService().translate(
            ocr_text,
            source_lang=source_lang,
            target_lang=target_lang,
        )

        return {
            "filename": safe_name,
            "file_path": str(target_path),
            "source_lang": source_lang,
            "target_lang": target_lang,
            "ocr_text": ocr_text,
            "translated_text": translated,
        }
