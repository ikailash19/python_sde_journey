# Database Fundamentals

## Why Databases?

Application memory is temporary.

Example:

```python
self.movies = {}
self.bookings = {}
```

When the application restarts:

```bash
uvicorn main:app --reload
```

all data is lost.

Databases provide persistent storage.

---

## Table

A table stores related data.

Example:

Movies

| movie_id | movie_name | total_seats |
|-----------|------------|-------------|
| 1 | Titanic | 30 |
| 2 | Avatar | 40 |

---

## Row

A single record inside a table.

Example:

| movie_id | movie_name | total_seats |
|-----------|------------|-------------|
| 1 | Titanic | 30 |

This is one row.

---

## Column

A field/property in a table.

Example:

```text
movie_id
movie_name
total_seats
```

---

## Primary Key

A unique identifier for each row.

Example:

```text
movie_id
```

Properties:

- Unique
- Not Null
- Identifies exactly one row

---

## Auto Increment IDs

Databases can generate IDs automatically.

Example:

```text
1
2
3
4
5
```

without application code maintaining counters.

---

## Foreign Key

A column that references another table.

Example:

Bookings Table

```text
movie_id
```

references:

Movies Table

```text
movie_id
```

Purpose:

- Prevent invalid references
- Maintain data integrity

---

## One-To-Many Relationship

Example:

```text
One Movie
     ↓
Many Bookings
```

Titanic:

```text
Seat 1
Seat 2
Seat 3
Seat 4
```

All belong to the same movie.

---

## Data Integrity

Foreign keys prevent invalid records.

Invalid Example:

```text
Booking
movie_id = 999
```

when Movie 999 does not exist.

The database rejects such records.

---

## In-Memory Storage vs Database

In-Memory:

```python
self.movies = {}
```

Pros:

- Fast
- Simple

Cons:

- Data lost after restart

Database:

```text
PostgreSQL
MySQL
SQL Server
MongoDB
```

Pros:

- Persistent storage
- Shared across servers
- Supports relationships
- Scalable

Cons:

- Additional setup and management