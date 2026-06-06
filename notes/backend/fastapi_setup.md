# FastAPI Setup

Status: Learning
Last Revised: 06-Jun-2026

Interview Confidence:
⭐

## What is FastAPI?

FastAPI is a modern Python web framework used to build APIs.

It allows backend functionality to be exposed through HTTP endpoints.

---

## Installation

```bash
pip install fastapi uvicorn
```

---

## First Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Kailash"}
```

---

## What is FastAPI()?

FastAPI() creates an application instance.

The app object represents the backend application and is used to register routes and API endpoints.

---

## What is @app.get("/")?

A decorator that maps a URL path to a Python function.

Example:

GET /

↓

home()

---

## Request Flow

Client
↓
HTTP Request
↓
FastAPI Route
↓
Function
↓
JSON Response
↓
Client

---

## Why does FastAPI return JSON automatically?

FastAPI automatically serializes Python dictionaries and lists into JSON responses.

It also sets:

Content-Type: application/json

This removes the need for manual JSON conversion.

---

## Backend Design Principle

Endpoints should remain thin.

Bad:

Endpoint contains validation, booking logic and database logic.

Good:

Endpoint
↓
Service Layer
↓
Database

Example:

@app.post("/book-seat/{seat_number}")

↓

booking_service.book_seat(...)