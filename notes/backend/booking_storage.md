# Booking Storage Design

Status: Learning
Last Revised: 09-Jun-2026

Interview Confidence:
⭐⭐⭐

---

# Why Store Bookings?

Previously:

```python
booking = Booking(...)
return booking
```

After returning, the booking could be lost.

We introduced storage:

```python
self.bookings = {}
```

inside BookingService.

---

# Booking Dictionary

Example:

```python
{
    1: booking1,
    2: booking2,
    3: booking3
}
```

Key:
- booking_id

Value:
- Booking object

---

# Why Dictionary?

Dictionary provides:

```python
self.bookings.get(booking_id)
```

Average Time Complexity:

```text
O(1)
```

List would require:

```python
for booking in bookings:
```

Time Complexity:

```text
O(n)
```

---

# Booking ID Ownership

Booking owns:

```python
booking_id
```

because it is a property of the booking.

---

# next_booking_id Ownership

BookingService owns:

```python
next_booking_id
```

because it controls booking creation.

---

# Collection Ownership

BookingService owns:

```python
self.bookings
```

because it manages all bookings.

Booking only represents a single booking.

---

# Current Flow

Client
↓
FastAPI
↓
BookingService
↓
Create Booking
↓
Store Booking
↓
Return Booking

---

# API Design

Request:

```http
GET /bookings/1
```

Returns:

```python
Booking Object
```

---

# Missing Booking

Bad:

```python
None
```

or

```python
"Booking not found"
```

Better:

```http
404 Not Found
```

This follows REST API standards.

---

# Key Concepts Learned

- Dictionary Storage
- O(1) Retrieval
- Collection Ownership
- Booking ID Generation
- API Error Handling
- HTTP 404