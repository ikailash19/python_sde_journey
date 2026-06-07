# FastAPI Movie Booking Integration

Status: Learning
Last Revised: 07-Jun-2026

Interview Confidence:
⭐⭐

---

# FastAPI + Business Logic

FastAPI endpoints should be thin.

Bad:

```python
@app.post("/book-seat/{seat_number}")
def book_seat(seat_number: int):

    spot = movie.get_seat(seat_number)

    if spot and not spot.is_booked:
        spot.book_seat()

    return True
```

The endpoint contains business logic.

Good:

```python
@app.post("/book-seat/{seat_number}")
def book_seat(seat_number: int):

    return booking_service.book_seat(
        movie,
        seat_number
    )
```

The endpoint delegates business logic to the service layer.

---

# Current Architecture

Client
↓
Uvicorn
↓
FastAPI
↓
Endpoint
↓
BookingService
↓
Movie
↓
Seat
↓
Response

---

# Path Parameters

Example:

```python
@app.get("/book-seat/{seat_number}")
def book_seat(seat_number: int):
```

Request:

```text
/book-seat/2
```

FastAPI extracts:

```python
seat_number = 2
```

and passes it to the function.

---

# Why seat_number: int?

URL values arrive as strings.

Example:

```text
/book-seat/2
```

arrives as:

```python
"2"
```

Without type conversion:

```python
movie.get_seat("2")
```

fails because dictionary keys are integers:

```python
{
    1: Seat(1),
    2: Seat(2)
}
```

FastAPI automatically converts:

```python
"2"
```

to:

```python
2
```

when we specify:

```python
seat_number: int
```

This is called type conversion and validation.

---

# Service Layer

A service layer contains business logic.

Example:

```python
BookingService
```

Responsibilities:

- Book seat
- Cancel booking
- Validate booking rules

The endpoint should call the service instead of implementing business logic itself.

---

# Why MovieService?

Current implementation:

```python
movies = []
```

Works for learning.

As the application grows:

```python
MovieService
```

can manage:

- Create movie
- Get movie
- Delete movie
- Update movie
- List movies

This follows separation of concerns.

---

# Single Responsibility Principle (SRP)

Each service should have one responsibility.

Bad:

```text
BookingService
├── Booking
├── User
├── Payment
├── Notification
├── Movie
```

Good:

```text
BookingService
UserService
PaymentService
NotificationService
MovieService
```

Each service owns a specific area of the application.

---

# Booking Object

Current:

```python
return True
```

Better:

```python
return Booking(...)
```

A Booking object can contain:

- booking_id
- movie
- seat
- booking_time
- status

This is how real-world ticket booking systems work.

---

# Uvicorn vs FastAPI

FastAPI:
- Backend framework
- Defines routes
- Contains business logic

Uvicorn:
- ASGI server (Asynchronous Server Gateway Interface)
- Runs FastAPI application
- Listens for HTTP requests
- Returns responses

Architecture:

Browser
↓
Uvicorn
↓
FastAPI
↓
Business Logic

---

# Key Concepts Learned

- FastAPI
- Uvicorn
- Routes
- Decorators
- JSON Responses
- Path Parameters
- Type Conversion
- Service Layer
- Single Responsibility Principle
- Backend Architecture
- Business Logic Separation