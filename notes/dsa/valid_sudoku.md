# Valid Sudoku

## Problem

Determine whether a partially filled Sudoku board is valid.

Rules:

- A number must not repeat in the same row.
- A number must not repeat in the same column.
- A number must not repeat in the same 3x3 box.
- Empty cells are represented using ".".

---

## Data Structure

HashSet

Used for fast duplicate detection.

Example:

```python
seen = set()

if value in seen:
    return False

seen.add(value)
```

Lookup Complexity:

```text
O(1)
```

---

## Row Validation

For each row:

```python
for row in range(9):
    seen = set()
```

Check for duplicate numbers while skipping ".".

---

## Column Validation

For each column:

```python
for col in range(9):
    seen = set()
```

Check for duplicate numbers while skipping ".".

---

## Box Validation

3x3 box starting positions:

```text
(0,0) (0,3) (0,6)

(3,0) (3,3) (3,6)

(6,0) (6,3) (6,6)
```

Traversal:

```python
for box_row in [0, 3, 6]:
    for box_col in [0, 3, 6]:
```

Visit all cells inside the box:

```python
for row in range(box_row, box_row + 3):
    for col in range(box_col, box_col + 3):
```

---

## Early Exit

As soon as a duplicate is found:

```python
return False
```

Avoids unnecessary work.

---

## Complexity

Generalized Board:

Time Complexity:

```text
O(n²)
```

Space Complexity:

```text
O(n)
```

Standard Sudoku:

```text
O(1)
```

because board size is fixed at 9x9.