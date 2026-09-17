
## EXISTS

`EXISTS` checks whether a subquery returns at least one row.

```sql
SELECT department_id, department_name
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.department_id
);
```

If the subquery returns at least one row → `TRUE`.

`SELECT 1` is commonly used because `EXISTS` only cares whether a row exists, not what value is returned.

---

## ANY

`ANY` compares a value against multiple values and returns `TRUE` if the comparison is `TRUE` for at least one value.

```sql
SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = 10
);
```

Example:

```text
55,000 > ANY (50,000, 60,000, 70,000)
```

Result:

```text
TRUE
```

Because 55,000 is greater than at least one value: 50,000.

Think:

```text
ANY → at least one
```

---

## ALL

`ALL` requires the comparison to be `TRUE` for every value returned by the subquery.

```sql
SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = 10
);
```

Example:

```text
55,000 > ALL (50,000, 60,000, 70,000)
```

Result:

```text
FALSE
```

Because 55,000 is not greater than 60,000 and 70,000.

Think:

```text
ALL → every one
```

### ANY vs ALL

```text
ANY → at least one
ALL → every one
```

---

## Correlated Subquery

A correlated subquery references a column from the outer query.

The inner query therefore depends on the current row being processed by the outer query.

### Employees earning above their own department average

```sql
SELECT employee_id,
       employee_name
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.department_id = e2.department_id
);
```

Here:

```text
Outer query → e1
Inner query → e2

e1.department_id = e2.department_id
```

The average salary is calculated for the current employee's department.

### Movie example

```sql
SELECT title,
       rating
FROM movies m1
WHERE rating > (
    SELECT AVG(rating)
    FROM movies m2
    WHERE m1.genre_id = m2.genre_id
);
```

This returns movies whose rating is above the average rating of their own genre.

---

# Set Operations

Set operations combine the results of multiple `SELECT` queries.

The participating queries must have compatible numbers and types of columns.

## UNION

Combines results and removes duplicates.

```sql
SELECT city
FROM customers

UNION

SELECT city
FROM suppliers;
```

## UNION ALL

Combines results and keeps duplicates.

```sql
SELECT city
FROM customers

UNION ALL

SELECT city
FROM suppliers;
```

`UNION ALL` generally avoids the duplicate-removal work performed by `UNION`.

## INTERSECT

Returns rows that exist in both result sets.

```sql
SELECT city
FROM customers

INTERSECT

SELECT city
FROM suppliers;
```

## EXCEPT

Returns rows from the first query that do not exist in the second query.

```sql
SELECT city
FROM customers

EXCEPT

SELECT city
FROM suppliers;
```

### Quick memory

```text
UNION       → A + B, remove duplicates
UNION ALL   → A + B, keep duplicates
INTERSECT   → common rows
EXCEPT      → A minus B
```

---

# ON DELETE and ON UPDATE

Foreign keys can define what happens to related rows when a referenced row is deleted or updated.

## RESTRICT

Prevents the parent row from being deleted or updated when dependent rows exist.

```sql
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id)
ON DELETE RESTRICT
```

Example:

```text
Customer
   ↓
Order
```

If an order references the customer, deleting that customer is prevented.

---

## CASCADE

Automatically applies the parent operation to dependent rows.

```sql
ON DELETE CASCADE
```

Deleting the parent can delete the related child rows.

Use carefully because one delete can affect many rows.

---

## SET NULL

Sets the foreign-key value in dependent rows to `NULL` when the referenced row is deleted or updated.

```sql
ON DELETE SET NULL
```

The foreign-key column must allow `NULL`.

---

## SET DEFAULT

Sets the foreign-key column to its defined default value.

```sql
ON DELETE SET DEFAULT
```

The resulting default value must satisfy the foreign-key constraint.

---

# PostgreSQL JSON and JSONB

## JSON vs JSONB

`JSON` stores the original JSON representation.

`JSONB` stores JSON in PostgreSQL's decomposed binary representation.

JSONB is generally preferable when JSON data needs to be queried, filtered, or indexed frequently.

---

# JSONB Operators

## `->`

Extracts a JSON/JSONB value while keeping it as JSON/JSONB.

```sql
profile -> 'address'
```

For a JSONB column, the result is JSONB.

---

## `->>`

Extracts a JSON value as text.

```sql
profile ->> 'city'
```

Important:

```text
->  → JSON/JSONB
->> → TEXT
```

Example:

```sql
SELECT profile ->> 'city'
FROM users;
```

---

## Nested JSONB Extraction

Example:

```json
{
  "name": "Kailash",
  "address": {
    "city": "Chennai",
    "pincode": "600001"
  }
}
```

Extract the nested city:

```sql
profile -> 'address' ->> 'city'
```

---

# Filtering JSONB

```sql
SELECT *
FROM users
WHERE profile ->> 'city' = 'Chennai';
```

Because `->>` returns text, this is a text comparison.

---

# JSONB Numeric Comparison

JSON values extracted using `->>` are text.

Therefore, cast when a numeric comparison is required.

```sql
SELECT *
FROM users
WHERE (profile ->> 'age')::int > 25;
```

---

# PostgreSQL Cast Operator `::`

`::` is PostgreSQL's explicit type-cast operator.

Examples:

```sql
'123'::int
'2026-09-17'::date
'25'::numeric
'25'::jsonb
```

Example:

```sql
(profile ->> 'age')::int
```

means:

```text
JSONB value
    ↓
->>
TEXT
    ↓
::int
INTEGER
```

Do not unnecessarily cast `->>` output to `TEXT` because `->>` already returns text.

---

# JSONB Containment — `@>`

`@>` checks whether the left JSONB value contains the JSON structure on the right.

```sql
SELECT *
FROM users
WHERE profile @> '{"city":"Chennai"}'::jsonb;
```

Multiple properties can be checked together:

```sql
SELECT *
FROM users
WHERE profile @> '{"city":"Chennai","role":"developer"}'::jsonb;
```

This checks that both properties are contained.

`@>` can also be combined with `OR`:

```sql
SELECT *
FROM users
WHERE profile @> '{"city":"Chennai"}'::jsonb
   OR profile @> '{"city":"Bangalore"}'::jsonb;
```

For simple scalar values, another clean option is:

```sql
WHERE profile ->> 'city' IN ('Chennai', 'Bangalore')
```

Choose the operator based on the structure and requirement, rather than simply whether the condition uses `AND` or `OR`.

---

# JSONB Existence Operators

## `?`

Checks whether a key exists at the top level.

```sql
profile ? 'city'
```

Example:

```sql
SELECT *
FROM users
WHERE profile ? 'skills';
```

`?` checks for a key, not a value.

```sql
profile ? 'Chennai'
```

does not check whether the value `Chennai` exists.

### Nested key

Given:

```json
{
  "address": {
    "city": "Chennai"
  }
}
```

This does not find `city`:

```sql
profile ? 'city'
```

Instead:

```sql
profile -> 'address' ? 'city'
```

---

## `?|`

Checks whether **ANY** of the specified keys exist.

Equivalent to an OR across the keys.

```sql
profile ?| ARRAY['phone', 'email', 'city']
```

Returns `TRUE` if at least one of those keys exists.

Example:

```sql
SELECT *
FROM users
WHERE profile ?| ARRAY['phone', 'email'];
```

---

## `?&`

Checks whether **ALL** of the specified keys exist.

Equivalent to an AND across the keys.

```sql
profile ?& ARRAY['name', 'city', 'age']
```

Example:

```sql
SELECT *
FROM users
WHERE profile ?& ARRAY['name', 'city'];
```

### Quick memory

```text
?   → one specified key
?|  → ANY keys → OR
?&  → ALL keys → AND
```

These existence operators check top-level keys unless you first navigate into a nested JSON object.

---

# GIN Indexes for JSONB

GIN = Generalized Inverted Index.

GIN is useful for searching inside composite values such as JSONB.

Example:

```sql
CREATE INDEX idx_users_profile
ON users
USING GIN (profile);
```

GIN indexes are useful for JSONB queries involving operators such as:

```text
@
@>
<@
?
?|
?&
```

depending on the operator class and index definition.

A GIN index does not guarantee PostgreSQL will use the index. The query planner chooses the execution strategy based on estimated cost.

---

# GIN Index Trade-offs

GIN indexes can provide faster searches for suitable JSONB queries, but require additional:

- Storage
- Index maintenance
- Write/update work

Therefore, do not automatically create a GIN index on every JSONB column.

A GIN index is more reasonable when:

```text
JSONB is queried frequently
+
JSONB filtering is important
+
The read-performance benefit justifies index maintenance
```

If a JSONB column is rarely queried but frequently updated, the GIN index may not be worthwhile.

---

# `jsonb_ops` vs `jsonb_path_ops`

Default JSONB GIN index:

```sql
CREATE INDEX idx_users_profile
ON users
USING GIN (profile);
```

This uses the general-purpose `jsonb_ops` operator class.

A specialized option:

```sql
CREATE INDEX idx_users_profile_path
ON users
USING GIN (profile jsonb_path_ops);
```

## `jsonb_ops`

General-purpose JSONB GIN operator class.

Provides broader JSONB operator support, including existence operators.

## `jsonb_path_ops`

Specialized GIN operator class focused primarily on JSONB containment using `@>`.

It can produce a smaller, more specialized index for suitable containment-heavy workloads.

Do not think of `jsonb_path_ops` as simply "the faster version." It trades broader operator support for specialization.

### Memory rule

```text
jsonb_ops
    → general-purpose JSONB GIN

jsonb_path_ops
    → specialized for @> containment
```

---

# EXPLAIN and JSONB Indexes

`EXPLAIN` shows PostgreSQL's planned execution strategy.

```sql
EXPLAIN
SELECT *
FROM users
WHERE profile @> '{"city":"Chennai"}'::jsonb;
```

A plan containing:

```text
Bitmap Index Scan on idx_users_profile
```

indicates that PostgreSQL chose to use the index.

---

# EXPLAIN ANALYZE

`EXPLAIN ANALYZE` actually executes the query and provides actual execution information.

```sql
EXPLAIN ANALYZE
SELECT *
FROM users
WHERE profile @> '{"city":"Chennai"}'::jsonb;
```

It can show:

- Actual rows
- Estimated rows
- Execution strategy
- Planning time
- Execution time

Remember:

```text
EXPLAIN
    → planned execution

EXPLAIN ANALYZE
    → executes query + reports actual execution
```

`EXPLAIN ANALYZE` executes the statement, so be especially careful with `UPDATE`, `DELETE`, and other modifying statements.

---

# Sequential Scan vs Index Scan

If `EXPLAIN` shows:

```text
Seq Scan on users
```

PostgreSQL is scanning the table sequentially and did not choose the available index.

This does NOT automatically mean the query is poorly optimized.

PostgreSQL may choose a sequential scan when:

- The table is small.
- A large percentage of rows match.
- Reading the entire table is estimated to be cheaper.
- The estimated index path has higher cost.

Core principle:

```text
Index exists
    ↓
Planner evaluates possible execution strategies
    ↓
Chooses the estimated cheapest plan
```

An index existing does not mean PostgreSQL should always use it.

---

# JSONB Expression Index

If the application frequently searches one specific JSONB property, an expression index can target that property directly.

Example query:

```sql
SELECT *
FROM users
WHERE profile ->> 'country' = 'India';
```

Expression index:

```sql
CREATE INDEX idx_users_country
ON users ((profile ->> 'country'));
```

The double parentheses are used because `profile ->> 'country'` is an expression rather than a simple column reference.

This defaults to a B-tree index and is appropriate for equality-style comparisons such as:

```sql
WHERE profile ->> 'country' = 'India';
```

### Why double parentheses?

```sql
ON users ((profile ->> 'country'))
```

The outer parentheses belong to the index-column/expression syntax.

The inner parentheses identify the expression.

For an expression index, the normal syntax is:

```sql
CREATE INDEX index_name
ON table_name ((expression));
```

---

# Partial Index on JSONB

A partial index contains only rows satisfying a specified condition.

Example:

```sql
CREATE INDEX idx_active_developers
ON users ((profile ->> 'role'))
WHERE (profile ->> 'active')::boolean = true;
```

This indexes only rows where `active` is `true`.

Conceptually:

```text
All users
    ↓
Rows satisfying partial-index WHERE condition
    ↓
Stored in the partial index
```

Partial indexes can reduce index size and maintenance compared with indexing every row when only a subset is relevant.

If JSON stores:

```json
{
  "active": "active"
}
```

then:

```sql
WHERE profile ->> 'active' = 'active'
```

is sufficient.

Because `->>` already returns TEXT, this is unnecessary:

```sql
(profile ->> 'active')::TEXT = 'active'
```

Casting to `TEXT` does not make the comparison safer.

If JSON stores an actual boolean:

```json
{
  "active": true
}
```

then:

```sql
WHERE (profile ->> 'active')::boolean = true
```

can be used when an actual boolean comparison is desired.

---

# Choosing a JSONB Index

| Requirement | Possible approach |
|---|---|
| Search many different properties inside JSONB | GIN |
| Mostly `@>` containment queries | GIN + `jsonb_path_ops` |
| Frequently search one JSONB property | Expression index |
| Frequently search only a subset of rows | Partial index |
| Rarely query JSONB but frequently update it | Consider avoiding GIN |

Always verify real query behavior with:

```sql
EXPLAIN ANALYZE
```

rather than assuming an index automatically improves performance.

---

# JSONB Operator Quick Reference

```text
->       → extract JSON/JSONB value
->>      → extract value as TEXT

@>       → left JSONB contains right JSONB
<@       → left JSONB is contained by right JSONB

?        → specified key exists
?|       → ANY specified keys exist
?&       → ALL specified keys exist

::       → explicit PostgreSQL type cast
```

## JSONB Index Quick Reference

```text
GIN
    → broad JSONB searching

jsonb_ops
    → general-purpose JSONB GIN operator class

jsonb_path_ops
    → specialized for @> containment

Expression index
    → target a specific JSONB expression/property

Partial index
    → target only a subset of rows

EXPLAIN
    → planned execution strategy

EXPLAIN ANALYZE
    → actual execution + performance information
```