# FastAPI Request Models

## What is a Request Model?

A Request Model defines the structure of incoming API data.

Example:

```python
class MovieRequest(BaseModel):
    movie_name: str
    total_seats: int
```

---

## Why Use Request Models?

Benefits:

- Input validation
- Type checking
- Cleaner APIs
- Automatic Swagger documentation

---

## What is Pydantic?

Pydantic is a Python library used by FastAPI for:

- Data validation
- Data parsing
- Type conversion

Example:

```json
{
    "movie_name": "Titanic",
    "total_seats": 30
}
```

FastAPI automatically converts this into:

```python
MovieRequest(
    movie_name="Titanic",
    total_seats=30
)
```

---

## Accessing Values

Since MovieRequest is an object:

```python
movie_request.movie_name
movie_request.total_seats
```

Not:

```python
movie_request["movie_name"]
```

---

## Validation

If:

```json
{
    "movie_name": "Titanic",
    "total_seats": "abc"
}
```

is sent,

Pydantic rejects the request and FastAPI returns:

```text
HTTP 422 Unprocessable Entity
```

before business logic executes.

---

## Swagger UI

FastAPI automatically generates API documentation.

URL:

```text
http://127.0.0.1:8000/docs
```

Features:

- View APIs
- Test APIs
- See request schemas
- See response schemas

---

## POST /movies Flow

```text
Client
  ↓
MovieRequest
  ↓
FastAPI Route
  ↓
MovieService
  ↓
Movie
  ↓
Response
```