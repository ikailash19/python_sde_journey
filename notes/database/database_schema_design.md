# Database Schema Design

## One Responsibility Per Table

A table should represent one concept.

Examples:

- Movies
- Seats
- Bookings

Avoid mixing unrelated data into the same table.

---

## Movies Table

| Column | Purpose |
|----------|----------|
| movie_id | Primary Key |
| movie_name | Movie Name |
| total_seats | Total Seats |

---

## Seats Table

| Column | Purpose |
|----------|----------|
| seat_id | Primary Key |
| movie_id | Foreign Key |
| seat_number | Display Seat Number |
| status | AVAILABLE / BOOKED |

Relationship:

```text
Many Seats
    ↓
One Movie
```

Foreign Key:

```text
Seats.movie_id
    ↓
Movies.movie_id
```

---

## Bookings Table

| Column | Purpose |
|----------|----------|
| booking_id | Primary Key |
| seat_id | Foreign Key |
| booking_time | Booking Timestamp |

Relationship:

```text
Many Bookings
    ↓
One Seat
```

---

## Why Separate Bookings Table?

Benefits:

- Separation of responsibility
- Better scalability
- Easier maintenance
- Supports booking history
- Cleaner schema design

---

## Primary Key

Properties:

- Unique
- Not Null
- Identifies exactly one row

Examples:

```text
movie_id
seat_id
booking_id
```

---

## Foreign Key

Used to create relationships between tables.

Examples:

```text
Seats.movie_id
    → Movies.movie_id

Bookings.seat_id
    → Seats.seat_id
```