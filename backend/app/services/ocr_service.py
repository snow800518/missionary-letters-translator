from __future__ import annotations

from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class OCRService:
    @staticmethod
    def extract_text(file_path: str | Path) -> str:
        file_path = Path(file_path)
        suffix = file_path.suffix.lower()

        if suffix in {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}:
            return OCRService._ocr_image(file_path)
        if suffix == ".pdf":
            return OCRService._ocr_pdf(file_path)

        return "Unsupported file type for OCR. Please upload PNG, JPG, TIFF, or PDF."

    @staticmethod
    def _ocr_image(image_path: Path) -> str:
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, config="--psm 6")
            return text.strip() or "No text detected. Try a sharper scan or different page orientation."
        except Exception as exc:
            return f"OCR failed for image: {exc}"

    @staticmethod
    def _ocr_pdf(pdf_path: Path) -> str:
        try:
            images = convert_from_path(str(pdf_path))
            pages = []
            for idx, image in enumerate(images, start=1):
                page_text = pytesseract.image_to_string(image, config="--psm 6")
                pages.append(f"[Page {idx}]\n{page_text.strip()}")
            return "\n\n".join(pages) if pages else "No pages were found in the PDF."
        except Exception as exc:
            return f"PDF OCR failed: {exc}"
