# SHL Conversational Assessment Recommender

## Features

- Conversational SHL assessment recommendations
- FastAPI backend
- Streamlit frontend
- RAG pipeline
- FAISS vector database
- Hybrid retrieval
- Prompt injection defense

---

# Installation

## Clone Repository

```bash
git clone <repo_url>
cd shl-assessment-agent
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

---

# Build Vector Database

```bash
python app/services/retriever.py
```

---

# Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://localhost:8000
```

---

# Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# API Endpoints

## Health Endpoint

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java developer"
    }
  ]
}
```

Response:

```json
{
  "reply": "Here are recommended SHL assessments.",
  "recommendations": [
    {
      "name": "Java 8 (New)",
      "url": "https://www.shl.com/...",
      "test_type": "K"
    }
  ],
  "end_of_conversation": true
}
```

---

# Run Tests

```bash
pytest
```

---

# Deployment

## Railway

```bash
railway up
```

## Docker

```bash
docker-compose up --build
```