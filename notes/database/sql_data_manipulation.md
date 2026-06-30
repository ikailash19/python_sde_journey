# SQL Data Manipulation

## UPDATE

Used to modify existing records.

Example:

```sql
UPDATE movies
SET total_seats = 100
WHERE movie_id = 2;
```

Always use a WHERE clause unless you intentionally want to update every row.

---

## DELETE

Used to remove rows from a table.

Example:

```sql
DELETE FROM movies
WHERE movie_id = 1;
```

DELETE removes rows but keeps the table structure.

---

## DROP TABLE

Deletes:

- Table
- Data
- Constraints
- Schema

Example:

```sql
DROP TABLE movies;
```

Use with caution.

---

## WHERE

Filters rows.

Example:

```sql
SELECT *
FROM movies
WHERE total_seats > 50;
```

WHERE is also commonly used with UPDATE and DELETE.

---

## ORDER BY

Sorts the result.

Descending:

```sql
SELECT *
FROM movies
ORDER BY total_seats DESC;
```

Ascending:

```sql
SELECT *
FROM movies
ORDER BY total_seats ASC;
```

ASC is the default.

---

## ALTER TABLE

Used to modify the structure of an existing table.

Example:

```sql
ALTER TABLE movies
ADD COLUMN rating DECIMAL(2,1);
```

Existing data remains unchanged.

---

## Safe SQL Workflow

For UPDATE or DELETE operations:

1. SELECT the target rows.
2. Verify the rows.
3. Execute UPDATE or DELETE.
4. SELECT again to verify the result.