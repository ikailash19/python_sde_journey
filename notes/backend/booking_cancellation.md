# Booking Cancellation Design

Status: Learning
Last Revised: 10-Jun-2026

Interview Confidence:
⭐⭐⭐

---

# Why Cancel Instead Of Delete?

Bad:

```python
del self.bookings[booking_id]
```

Problem:

- Booking history lost
- No audit trail
- No customer support reference

---

# Better Approach

```python
booking.status = "CANCELLED"
```

Keep booking record.

Benefits:

- History preserved
- Reporting possible
- Analytics possible
- Customer support possible

---

# Seat Release

When booking is cancelled:

```python
booking.status = "CANCELLED"
booking.seat.unbook_seat()
```

Seat becomes available again.

---

# BookingService Responsibility

BookingService coordinates:

- Booking
- Seat

Cancellation affects multiple entities.

Therefore cancellation logic belongs to:

```python
BookingService
```

not Booking.

---

# Double Cancellation

Current:

```text
BOOKED
↓
CANCELLED
```

Valid.

Second cancellation:

```text
CANCELLED
↓
CANCELLED
```

Should fail.

Reason:

Booking is already cancelled.

---

# HTTP Status Codes

Booking not found:

```http
404 Not Found
```

Already cancelled:

```http
400 Bad Request
```

---

# Enum Improvement

Current:

```python
"BOOKED"
"CANCELLED"
```

Better:

```python
BookingStatus.BOOKED
BookingStatus.CANCELLED
```

Benefits:

- Avoid typos
- Better maintainability
- Industry standard