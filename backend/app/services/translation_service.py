from __future__ import annotations

from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_BASE_URL


class TranslationService:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL) if OPENAI_API_KEY else None

    def translate(self, text: str, source_lang: str = "en", target_lang: str = "ko") -> str:
        if not text or not text.strip():
            return ""

        if self.client is None:
            return self._mock_translation(text, source_lang, target_lang)

        try:
            response = self.client.responses.create(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system",
                        "content": "You are a careful translator of historical and handwritten missionary documents. Preserve the meaning, names, historical tone, and readability.",
                    },
                    {
                        "role": "user",
                        "content": f"Translate the following {source_lang} text into {target_lang}. Preserve names, places, and historical phrasing when possible.\n\n{text}",
                    },
                ],
            )
            return response.output_text.strip()
        except Exception:
            return self._mock_translation(text, source_lang, target_lang)

    @staticmethod
    def _mock_translation(text: str, source_lang: str, target_lang: str) -> str:
        prefix = f"[Local fallback translation: {source_lang} -> {target_lang}]\n"
        return prefix + text
