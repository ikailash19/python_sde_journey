# Booking Entity Design

Status: Learning
Last Revised: 08-Jun-2026

Interview Confidence:
⭐⭐

---

# Why Booking Entity?

Initially our booking flow returned:

```python
True
False
```

This only tells us whether the booking succeeded.

A real-world backend needs more information:

- Which booking was created?
- Which movie was booked?
- Which seat was booked?
- When was it booked?
- What is the current booking status?

For this reason we introduced a Booking entity.

---

# Booking Entity

Current implementation:

```python
class Booking:

    def __init__(
        self,
        booking_id,
        movie,
        seat,
        booking_time,
        status
    ):
        self.booking_id = booking_id
        self.movie = movie
        self.seat = seat
        self.booking_time = booking_time
        self.status = status
```

---

# Booking Fields

## booking_id

Unique identifier for each booking.

Examples:

```text
1
2
3
```

In future this may be:

- Auto Increment ID
- UUID
- Database Generated ID

---

## movie

Stores the Movie object.

Example:

```python
booking.movie.movie_name
```

Benefits:

- Direct access to movie details
- Better object relationships
- Cleaner OOP design

---

## seat

Stores the Seat object.

Example:

```python
booking.seat.seat_number
```

Benefits:

- Direct access to seat details
- Avoids unnecessary lookups

---

## booking_time

Stores the timestamp when the booking was created.

Example:

```python
datetime.now()
```

Ownership:

```text
Booking owns booking_time
```

Reason:

Booking time describes the booking itself.

---

## status

Stores current booking state.

Examples:

```text
BOOKED
CANCELLED
```

Future examples:

```text
IN_PROGRESS
EXPIRED
REFUNDED
```

Ownership:

```text
Booking owns status
```

Reason:

Status describes the booking state.

---

# Has-A Relationships

Current design:

```text
Movie
 ↓
Seat
```

Movie has Seats.

---

```text
Booking
 ↓
Movie
```

Booking has a Movie.

---

```text
Booking
 ↓
Seat
```

Booking has a Seat.

---

These are called:

```text
Has-A Relationships
```

Examples:

- Car has an Engine
- Company has Employees
- Movie has Seats
- Booking has Movie
- Booking has Seat

---

# Entity vs Service

Important backend design principle.

---

## Entity

Stores data and state.

Examples:

```text
Movie
Seat
Booking
```

Entity examples:

```python
booking_id
movie
seat
booking_time
status
```

---

## Service

Performs actions and business logic.

Example:

```python
BookingService
```

Responsibilities:

```text
Book Seat
Cancel Booking
Validate Booking Rules
```

Services should not own booking data.

Entities should own data.

---

# Current Booking Flow

```text
Client
 ↓
FastAPI Endpoint
 ↓
BookingService
 ↓
Movie.get_seat()
 ↓
Seat.book_seat()
 ↓
Booking Created
 ↓
Booking Returned
```

---

# Current BookingService

```python
def book_seat(self, movie, seat):

    spot = movie.get_seat(seat)

    if spot is None:
        return False

    if spot.is_booked:
        return False

    spot.book_seat()

    booking = Booking(
        1,
        movie,
        spot,
        datetime.now(),
        "BOOKED"
    )

    return booking
```

---

# Design Improvement Identified

Current:

```python
Booking(1, ...)
```

Every booking receives:

```text
booking_id = 1
```

Future improvement:

```python
self.next_booking_id = 1
```

Generate:

```text
Booking 1
Booking 2
Booking 3
...
```

---

# Important Lesson Learned

Avoid creating Booking before validation.

Bad:

```python
Booking(...)
Validate Seat
```

Good:

```python
Validate Seat
Create Booking
```

Only create business objects after validation succeeds.

---

# FastAPI Bug Discovered

Error:

```text
AttributeError: 'bool' object has no attribute 'status'
```

Cause:

```python
Success -> Booking Object
Failure -> False
```

This creates mixed return types.

Example:

```python
booking = booking_service.book_seat(...)

booking.status
```

fails when:

```python
booking = False
```

This is a common backend integration issue.

---

# Key Concepts Learned

- Booking Entity
- Entity vs Service
- Has-A Relationship
- Object Ownership
- booking_time Ownership
- status Ownership
- Business Objects
- FastAPI Integration
- Mixed Return Type Bug
- Backend Design Principles

---

# Interview Takeaway

A backend engineer should model real-world concepts as entities.

Instead of:

```python
return True
```

Prefer:

```python
return Booking(...)
```

because business objects carry useful information and make systems easier to extend.