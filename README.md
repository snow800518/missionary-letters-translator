# missionary-letters-translator

A full-stack application for transcribing and translating early Korean missionary handwritten English letters and historical documents.

## Overview

This project combines:
- OCR for handwritten historical documents
- preprocessing for scans and paper artifacts
- translation workflow for English/Korean document processing
- a simple web interface for upload, review, and export

## Architecture

- Backend: FastAPI + Python
- Frontend: React + Vite
- OCR: Tesseract / EasyOCR support
- Translation: OpenAI-compatible API or local placeholder flow
- Storage: local uploads directory

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3) Access

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Swagger: http://localhost:8000/docs

## Environment variables

Create `backend/.env` with:

```env
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
````

If no API key is configured, the translation service will return a placeholder translation for local development and testing.

## Example API

```bash
curl -X POST "http://localhost:8000/api/documents/process" \
  -F "file=@sample.jpg" \
  -F "source_lang=en" \
  -F "target_lang=ko"
```

## Project status

This repository is intentionally scaffolded for practical development. It includes:
- OCR pipeline foundation
- translation API hook
- document upload workflow
- browser-based review interface

## Planned enhancements

- stronger handwriting models for older English cursive
- page-level preprocessing for damaged paper
- term dictionary for missionary names, locations, and historical vocabulary
- PDF export and manual correction workflow
- model benchmarking by document type
