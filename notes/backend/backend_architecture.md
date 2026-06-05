# Backend Architecture

Status: Learning
Last Revised: 05-Jun-2026

Interview Confidence:
⭐

## Typical Request Flow

Client
↓
HTTP Request
↓
FastAPI Endpoint
↓
Service Layer
↓
Database
↓
JSON Response
↓
Client

---

## What is an Entity?

An entity represents business data.

Examples:

Movie,
Seat,
User,
Booking.

Entities store data and business state.

---

## What is a Service Layer?

A service layer contains business logic.

Examples:

BookingService

Responsibilities:

- Booking seats
- Cancelling bookings
- Validation
- Coordinating entities

Benefits:

- Cleaner code
- Reusable logic
- Easier testing
- Better maintainability

---

## Why Not Put Everything in Endpoints?

Bad:

Endpoint contains database access, validation, and business logic.

Good:

Endpoint
↓
Service
↓
Database

Benefits:

- Smaller endpoints
- Reusable business logic
- Easier testing
- Better separation of concerns

---

## Validation

Objects should protect themselves from invalid state.

Example:

Movie("Titanic", -5)

Should not be allowed.

Validation should happen when creating the object.

Example:

if total_seats <= 0:
    raise ValueError()

Principle:

An object should never exist in an invalid state.

---

## Interview Questions

Q: What is an entity?

Q: What is a service layer?

Q: Why use a service layer?

Q: Why not put all logic in FastAPI endpoints?

Q: Where should validation happen?

Q: What is separation of concerns?