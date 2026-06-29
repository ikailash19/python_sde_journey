# PostgreSQL Basics

## What is PostgreSQL?

PostgreSQL is an open-source Relational Database Management System (RDBMS).

It stores data permanently and executes SQL statements.

---

## SQL vs PostgreSQL

SQL

- A language used to communicate with relational databases.

PostgreSQL

- A database management system that understands SQL and stores data.

---

## Architecture

Frontend
↓
FastAPI
↓
PostgreSQL
↓
Disk Storage

The frontend should never communicate directly with the database.

---

## Database Responsibilities

- Store data permanently
- Generate IDs
- Maintain relationships
- Enforce constraints
- Execute SQL queries
- Handle concurrent access

---

## GENERATED ALWAYS AS IDENTITY

Example:

```sql
movie_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
```

Meaning:

INTEGER

- Store whole numbers.

GENERATED

- Database generates the value.

ALWAYS

- The application should not provide the value.

AS IDENTITY

- Automatically generates increasing IDs.

PRIMARY KEY

- Unique
- Not Null
- Identifies each row

---

## First SQL Commands

Create table

```sql
CREATE TABLE movies (
    movie_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    movie_name TEXT NOT NULL,
    total_seats INTEGER NOT NULL CHECK (total_seats > 0)
);
```

Insert data

```sql
INSERT INTO movies (
    movie_name,
    total_seats
)
VALUES (
    'Titanic',
    30
);
```

Read data

```sql
SELECT * FROM movies;
```

---

## Engineering Principles Learned

- Database owns ID generation.
- Backend owns business logic.
- Frontend communicates only with the backend.
- Validate data in both FastAPI and the database.
- Let the database perform searching instead of loading unnecessary data into Python.