# Longest Common Prefix

## Problem

Given an array of strings, find the longest common prefix shared by all strings.

Example:

```python
["flower", "flow", "flight"]
```

Output:

```python
"fl"
```

---

## Approach

1. Assume the first string is the common prefix.
2. Compare it with every remaining string.
3. Shrink the prefix whenever a mismatch is found.
4. Continue until all strings are processed.

---

## Complexity

Time Complexity:

```text
O(n * m)
```

where:

- n = number of strings
- m = length of shortest string

Space Complexity:

```text
O(1)
```

---

## Key Learning

- Not every problem needs O(log n).
- O(n * m) is optimal for this problem.
- Compare characters until a mismatch is found.
- Keep shrinking the common prefix.

---

## Edge Case

```python
[]
```

Return:

```python
""
```

to avoid:

```python
IndexError
```

when accessing:

```python
strs[0]
```

---

## Interview Explanation

We use the first string as the initial prefix. For every remaining string, we compare characters one by one and shrink the prefix whenever a mismatch occurs. After processing all strings, the remaining prefix is the longest common prefix.