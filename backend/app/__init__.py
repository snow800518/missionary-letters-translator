from __future__ import annotations

from pydantic import BaseModel


class DocumentProcessRequest(BaseModel):
    source_lang: str = "en"
    target_lang: str = "ko"
