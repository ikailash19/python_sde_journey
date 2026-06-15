# Request & Response Models

## Pydantic BaseModel

Pydantic BaseModel is used to validate, parse and serialize data in FastAPI.

Example:

```python
from pydantic import BaseModel

class MovieRequest(BaseModel):
    movie_name: str
    total_seats: int
```

Benefits:

- Automatic validation
- Type conversion
- JSON parsing
- Swagger/OpenAPI schema generation

---

## Validation

Valid Request:

```json
{
  "movie_name": "Titanic",
  "total_seats": 30
}
```

Invalid Request:

```json
{
  "movie_name": "Titanic",
  "total_seats": "abc"
}
```

Response:

```http
422 Unprocessable Entity
```

---

## Type Conversion

Pydantic automatically converts compatible types.

Input:

```json
{
  "total_seats": "30"
}
```

Converted To:

```python
total_seats = 30
```

---

## Schema

A schema defines the structure of data.

Example:

```python
class BookingRequest(BaseModel):
    movie_id: int
    seat_number: int
```

Schema:

```text
movie_id    -> integer
seat_number -> integer
```

---

## OpenAPI

OpenAPI is a standard specification describing:

- API endpoints
- Request schemas
- Response schemas
- Parameters
- Status codes

FastAPI automatically generates OpenAPI definitions.

---

## Swagger

Swagger UI reads OpenAPI definitions and generates interactive API documentation.

Default URL:

```text
http://127.0.0.1:8000/docs
```

---

## Serialization

Conversion of Python objects into JSON.

Example:

```python
booking
```

↓

```json
{
  "booking_id": 1,
  "status": "BOOKED"
}
```

---

## Deserialization

Conversion of JSON into Python objects.

Example:

```json
{
  "movie_id": 1,
  "seat_number": 5
}
```

↓

```python
BookingRequest(
    movie_id=1,
    seat_number=5
)
```

---

## Request Models

Used for incoming API requests.

Example:

```python
class BookingRequest(BaseModel):
    movie_id: int
    seat_number: int
```

---

## Response Models

Used to control what data is returned to API consumers.

Example:

```python
class BookingResponse(BaseModel):
    booking_id: int
    status: str
```

Benefits:

- Hides internal fields
- Stable API contract
- Smaller responses
- Better frontend integration