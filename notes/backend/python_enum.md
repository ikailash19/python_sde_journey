# Python Enum

Status: Learning
Last Revised: 11-Jun-2026

Interview Confidence:
⭐⭐⭐

---

# What Is Enum?

Enum (Enumeration) is used to define a fixed set of allowed values.

Example:

```python
from enum import Enum

class BookingStatus(Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"
```

---

# Why Use Enum?

Bad:

```python
booking.status = "BOOKED"
booking.status = "BOOKD"
booking.status = "Cancelled"
```

Typos are possible.

Better:

```python
booking.status = BookingStatus.BOOKED
```

Invalid values fail immediately.

---

# Benefits

- Type Safety
- Avoid Typos
- Better Auto-complete
- Easier Refactoring
- Industry Standard

---

# Accessing Enum Values

Enum Object:

```python
BookingStatus.BOOKED
```

Underlying Value:

```python
BookingStatus.BOOKED.value
```

Result:

```python
"BOOKED"
```

---

# Comparison

Bad:

```python
if booking.status == "CANCELLED":
```

Better:

```python
if booking.status == BookingStatus.CANCELLED:
```

---

# Enum Inheritance

```python
class BookingStatus(Enum):
```

BookingStatus inherits from Enum.

This provides enum behavior without writing __init__.

---

# Project Usage

Used in Movie Booking application to represent booking states:

- BOOKED
- CANCELLED