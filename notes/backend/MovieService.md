# MovieService

## Why MovieService?

Instead of allowing FastAPI to directly manage Movie objects, we introduce a service layer.

Architecture:

```text
FastAPI
    ↓
MovieService
    ↓
Movie
```

Benefits:

- Separation of responsibilities
- Easier maintenance
- Better scalability
- Consistent architecture

---

## Movie Ownership

Movie should own:

```python
movie_id
movie_name
total_seats
seats
```

Reason:

- movie_id is a property of Movie.
- Similar to Booking owning booking_id.
- Consistent design.

---

## MovieService Responsibilities

```python
create_movie()
get_movie()
get_all_movies()
```

---

## Internal Storage

```python
self.movies = {}
```

Example:

```python
{
    1: Titanic,
    2: Interstellar
}
```

Movie ID is used as the key.

---

## Why movie_id Instead of movie_name?

Movie names may not be unique.

Example:

```text
Titanic
Titanic Re-release
```

Movie IDs guarantee uniqueness.

---

## Dictionary Iteration Learning

Returning:

```python
self.movies
```

and iterating over it:

```python
for movie in self.movies:
```

returns:

```python
1
2
3
```

because dictionaries iterate over keys by default.

---

## Correct Approach

```python
self.movies.values()
```

returns Movie objects.

---

## list() vs []

### Incorrect

```python
[self.movies.values()]
```

Result:

```python
[
    dict_values([...])
]
```

A list containing one element.

---

### Correct

```python
list(self.movies.values())
```

Result:

```python
[
    movie1,
    movie2
]
```

Converts all values into a list.

---

## Key Learning

```python
list(x)
```

means:

```text
Convert x into a list
```

while:

```python
[x]
```

means:

```text
Create a list containing x as a single element
```