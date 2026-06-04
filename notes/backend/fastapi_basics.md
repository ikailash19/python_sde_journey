# FastAPI Basics

Status: Learning
Last Revised: 04-Jun-2026

Interview Confidence:
⭐

## What is FastAPI?

FastAPI is a modern Python framework used to build APIs.

It allows backend functionality to be exposed through HTTP endpoints.

Example:

GET /movies

POST /movies

POST /book-seat

---

## What is an API?

API (Application Programming Interface) is a communication bridge between client and server.

Frontend
↓
API
↓
Backend
↓
Database

---

## What is an Endpoint?

An endpoint is a URL exposed by an API that clients can use to access backend functionality.

Examples:

GET /movies

POST /movies

GET /users

POST /bookings

---

## Common HTTP Methods

GET

Retrieve data.

Example:

GET /movies

---

POST

Create data.

Example:

POST /movies

POST /bookings

---

PUT

Replace an entire resource.

Example:

PUT /users/1

---

PATCH

Update selected fields only.

Example:

PATCH /users/1

---

DELETE

Remove a resource.

Example:

DELETE /movies/1

---

Interview Question

Q: Why should booking a seat use POST instead of GET?

A:

Booking a seat changes application state and creates a booking record. GET should only retrieve data and should not modify server state.