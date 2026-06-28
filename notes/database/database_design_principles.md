# Database Design Principles

## Defense in Depth

Business rules should be validated in multiple layers.

Example:

- FastAPI / Pydantic
- Database Constraints

This protects data integrity even if one layer fails.

---

## Race Condition

A race condition occurs when two or more operations happen at nearly the same time and the final result depends on which operation finishes first.

Example:

Two users try to book the last available seat simultaneously.

Without proper protection, both bookings may succeed.

---

## Database Responsibilities

The database should handle:

- Persistent storage
- Primary Key generation
- Foreign Key relationships
- Constraints
- Efficient searching
- Concurrent access

---

## Application Responsibilities

The application should handle:

- Request validation
- Business logic
- API responses
- Authentication
- Authorization

---

## Scalability Principle

Do not load unnecessary data into the application.

Instead of:

- Load all records
- Filter in Python

Prefer:

- Let the database filter
- Return only the required rows

Databases are optimized for querying large datasets.