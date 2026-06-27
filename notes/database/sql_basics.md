# SQL Basics

## CREATE TABLE

Used to create a new table inside a database.

Example:

```sql
CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    movie_name TEXT NOT NULL,
    total_seats INTEGER NOT NULL CHECK (total_seats > 0)
);
```

---

## INSERT

Used to insert rows into a table.

Example:

```sql
INSERT INTO movies(movie_id, movie_name, total_seats)
VALUES (1, 'Titanic', 30);
```

---

## Structure vs Data

CREATE TABLE

- Creates the table structure (schema)
- Defines columns
- Defines data types
- Defines constraints

INSERT

- Adds actual data into the table.

---

## Constraints Learned

PRIMARY KEY

- Unique
- Not Null
- Identifies a row

NOT NULL

- Value is required.

CHECK

- Enforces a business rule.

Example:

```sql
CHECK (total_seats > 0)
```

---

## Why Databases?

Python objects exist only while the application is running.

A database stores data permanently, so information remains available even after restarting the application.

This is called **persistent storage**.