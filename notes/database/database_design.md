# PostgreSQL Database Design

## 1. Database Normalization

Normalization is the process of structuring data to:

- Reduce duplicate data
- Prevent update anomalies
- Prevent insert anomalies
- Prevent delete anomalies
- Maintain data consistency

---

## 2. Database Anomalies

### Update Anomaly

The same information exists in multiple rows, so one logical change requires multiple updates.

Example:

```text
movie_id | genre
---------+--------
1        | Sci-Fi
2        | Sci-Fi
3        | Sci-Fi
```

Changing `Sci-Fi` to `Science Fiction` requires updating multiple rows.

### Insert Anomaly

A piece of information cannot be inserted without also providing unrelated information.

### Delete Anomaly

Deleting one record unintentionally removes other useful information.

---

# Normal Forms

## 3. First Normal Form (1NF)

A table is in 1NF when each column contains **atomic values**.

### Violates 1NF

```text
movie_id | title      | genres
---------+------------+-------------------
1        | Inception  | Sci-Fi, Thriller
```

The `genres` column contains multiple values.

### Better

```text
movie_id | title      | genre
---------+------------+----------
1        | Inception  | Sci-Fi
1        | Inception  | Thriller
```

### Mental Model

> **1NF → One cell = one value**

---

## 4. Second Normal Form (2NF)

A table is in 2NF when:

1. It is already in 1NF.
2. Every non-key column depends on the **entire primary key**.

This mainly matters when the table has a **composite primary key**.

Example:

```text
movie_actors

movie_id (PK)
actor_id (PK)
movie_title
```

Composite key:

```text
(movie_id, actor_id)
```

But:

```text
movie_id → movie_title
```

`movie_title` depends only on `movie_id`, not on the entire composite key.

This is a **partial dependency** and violates 2NF.

### Fix

Move `movie_title` to the appropriate table:

```text
movies
----------------
movie_id (PK)
movie_title

movie_actors
----------------
movie_id (PK, FK)
actor_id (PK, FK)
```

### Mental Model

> **2NF → Non-key columns must depend on the whole composite key.**

---

## 5. Third Normal Form (3NF)

A table is in 3NF when:

1. It is already in 2NF.
2. Non-key columns depend only on the primary key, not on another non-key column.

Example:

```text
movies

movie_id (PK)
movie_title
genre_id
genre_name
```

Dependencies:

```text
movie_id → genre_id
genre_id → genre_name
```

Therefore:

```text
movie_id → genre_name
```

indirectly.

This is a **transitive dependency** and violates 3NF.

### Fix

Separate the genre information:

```text
movies
----------------
movie_id (PK)
movie_title
genre_id (FK)

genres
----------------
genre_id (PK)
genre_name
```

### Mental Model

```text
1NF → Atomic values

2NF → Depend on the whole key

3NF → Depend only on the key, not another non-key column
```

---

# Relationships and Cardinality

## 6. One-to-Many (1:N)

One row in the parent table can relate to many rows in the child table.

Example:

```text
genres (1) ───────< movies (N)
```

One genre can contain many movies.

The foreign key normally goes on the **many side**:

```text
movies
----------------
movie_id (PK)
genre_id (FK)
```

### Mental Model

> **1:N → FK on the MANY side**

---

## 7. One-to-One (1:1)

One row in one table relates to at most one row in another table.

Example:

```text
users (1) ─────── 1 user_profiles
```

A common implementation is using one table's primary key as a foreign key:

```sql
user_id INT PRIMARY KEY REFERENCES users(user_id)
```

---

## 8. Many-to-Many (M:N)

Many rows in one table can relate to many rows in another table.

Example:

```text
movies (M) ─── movie_actors ─── (N) actors
```

A junction/bridge table is used:

```text
movie_actors
----------------
movie_id (PK, FK)
actor_id (PK, FK)
```

### Mental Model

> **M:N → Junction table**

---

# Junction Tables

## 9. Why Junction Tables Are Needed

Suppose:

- One movie has many actors.
- One actor can act in many movies.

Putting `actor_id` directly inside `movies` does not properly represent the M:N relationship.

Instead:

```text
movies
----------------
movie_id (PK)

actors
----------------
actor_id (PK)

movie_actors
----------------
movie_id (PK, FK)
actor_id (PK, FK)
```

---

## 10. Composite Primary Key

A table can have only **one primary key constraint**, but that constraint can contain multiple columns.

Example:

```sql
PRIMARY KEY (movie_id, actor_id)
```

This is a **composite primary key**.

It means the combination must be unique.

Valid:

```text
movie_id | actor_id
---------+---------
1        | 10
1        | 20
2        | 10
```

Invalid:

```text
movie_id | actor_id
---------+---------
1        | 10
1        | 10
```

The combination `(1, 10)` appears twice.

### Important

Two separate primary keys:

```text
movie_id → PK
actor_id → PK
```

is not what we mean here.

Instead:

```text
PRIMARY KEY (movie_id, actor_id)
```

is **one composite primary key constraint**.

---

# Constraints

## 11. Primary Key

A primary key uniquely identifies each row.

```sql
movie_id INT PRIMARY KEY
```

A primary key guarantees:

- Unique values
- No `NULL` values

A table can have only **one primary key constraint**, but it can be composite.

### Mental Model

> **PRIMARY KEY → Unique identity of a row**

---

## 12. Foreign Key

A foreign key creates a relationship with another table and enforces referential integrity.

```sql
genre_id INT REFERENCES genres(genre_id)
```

The value must reference an existing `genres.genre_id`, unless the column allows `NULL`.

### Mental Model

```text
PRIMARY KEY → Who am I?

FOREIGN KEY → Which row in another table do I reference?
```

---

## 13. UNIQUE

`UNIQUE` prevents duplicate values.

```sql
email TEXT UNIQUE
```

A table can have **multiple UNIQUE constraints**.

Example:

```sql
email TEXT UNIQUE,
phone TEXT UNIQUE
```

Each column independently enforces uniqueness.

### Mental Model

> **UNIQUE → Prevent duplicate values**

---

## 14. NOT NULL

`NOT NULL` ensures a column must contain a value.

```sql
title TEXT NOT NULL
```

This is rejected:

```sql
INSERT INTO movies (movie_id, title)
VALUES (1, NULL);
```

### Important

`NOT NULL` prevents `NULL`, but it does not prevent an empty string.

```text
NULL → ❌
''   → ✅
```

To reject both:

```sql
title TEXT NOT NULL
    CHECK (title <> '')
```

### Mental Model

> **NOT NULL → This field is mandatory**

---

## 15. CHECK

`CHECK` ensures that data satisfies a condition.

Example:

```sql
rating INT CHECK (rating BETWEEN 0 AND 10)
```

Valid:

```text
rating = 0  → ✅
rating = 8  → ✅
rating = 10 → ✅
```

Invalid:

```text
rating = -1 → ❌
rating = 11 → ❌
```

`BETWEEN` is inclusive.

For example:

```sql
CHECK (age BETWEEN 18 AND 60)
```

means:

```text
18 ≤ age ≤ 60
```

### Mental Model

> **CHECK → Data must satisfy this condition**

---

# Optional vs Mandatory Relationships

## 16. Mandatory Relationship

If every movie must have a genre:

```sql
genre_id INT NOT NULL
    REFERENCES genres(genre_id)
```

This enforces:

- `NOT NULL` → movie must have a genre
- `FOREIGN KEY` → referenced genre must exist

---

## 17. Optional Relationship

If a movie may exist without a genre:

```sql
genre_id INT REFERENCES genres(genre_id)
```

Because `NOT NULL` is not specified, `NULL` is allowed.

### Mental Model

```text
Mandatory relationship
→ NOT NULL + FOREIGN KEY

Optional relationship
→ FOREIGN KEY with NULL allowed
```

---

# Practical Database Design

## 18. Movie / Actor Schema

Requirement:

> A movie belongs to one genre. A genre can contain many movies. A movie can have many actors, and an actor can act in many movies.

Normalized design:

```text
genres
----------------
genre_id (PK)
genre_name

movies
----------------
movie_id (PK)
movie_title
genre_id (FK → genres.genre_id)

actors
----------------
actor_id (PK)
actor_name

movie_actors
----------------
movie_id (PK, FK → movies.movie_id)
actor_id (PK, FK → actors.actor_id)
```

Relationships:

```text
genres (1) ───────< movies (N)

movies (M) ───────< movie_actors >─────── (M) actors
```

---

## 19. Customer / Order / Product Schema

Requirement:

> A customer can place many orders. Each order belongs to one customer. An order can contain many products, and a product can appear in many orders.

Normalized design:

```text
customers
----------------
customer_id (PK)

orders
----------------
order_id (PK)
customer_id (FK → customers.customer_id)

products
----------------
product_id (PK)

order_items
----------------
order_id (PK, FK → orders.order_id)
product_id (PK, FK → products.product_id)
quantity
```

Relationships:

```text
customers (1) ───────< orders (N)

orders (M) ───────< order_items >─────── (M) products
```

`order_items` is required because Orders ↔ Products is an M:N relationship.

---

# Quick Interview Summary

```text
Normalization
→ Reduce redundancy and prevent anomalies

1NF
→ Atomic values
→ One cell = one value

2NF
→ No partial dependency
→ Non-key columns depend on the whole composite key

3NF
→ No transitive dependency
→ Non-key columns depend only on the key

1:1
→ One-to-one relationship

1:N
→ FK normally goes on the MANY side

M:N
→ Use a junction table

Composite PK
→ One primary key constraint containing multiple columns

PRIMARY KEY
→ Unique row identity

FOREIGN KEY
→ Valid reference to another table

UNIQUE
→ Prevent duplicate values

NOT NULL
→ Value is mandatory

CHECK
→ Value must satisfy a condition

Mandatory relationship
→ NOT NULL + FOREIGN KEY

Optional relationship
→ FOREIGN KEY with NULL allowed
```

# Key Takeaways

1. **1NF → Atomic values.**
2. **2NF → Depend on the whole composite key.**
3. **3NF → No transitive dependency.**
4. **1:N → FK normally belongs on the many side.**
5. **M:N → Use a junction table.**
6. A table has one primary key constraint, but it can be a **composite primary key**.
7. `PRIMARY KEY` identifies a row.
8. `FOREIGN KEY` maintains referential integrity.
9. `UNIQUE` prevents duplicates.
10. `NOT NULL` prevents missing values.
11. `CHECK` enforces data/business rules.
12. `NOT NULL + FOREIGN KEY` can enforce a mandatory relationship.
13. Good database design separates different entities into appropriate tables.