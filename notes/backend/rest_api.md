# REST API

Status: Learning
Last Revised: 24-May-2026

Interview Confidence:
⭐

## What is API?

API (Application Programming Interface) is a contract/interface that allows systems to communicate with each other.

Flow:

Frontend ->
API ->
Backend -> 
Database

Analogy:

API is like a waiter between customer and kitchen.

Customer gives request → waiter carries request → kitchen processes → waiter returns response.

---

## What is REST?

REST (Representational State Transfer) is a set of architectural rules/best practices used to design APIs.

REST principles:

- Resources represented using URLs
- Uses HTTP methods correctly
- Stateless communication
- Client-server separation

Examples:

GET /books

POST /books

PUT /books/1

DELETE /books/1

Instead of:

/getBooksDataNow

/deleteBookImmediately

REST creates cleaner APIs.

---

## Common HTTP Methods

GET

Retrieve data

Example:

GET /books

POST

Create data

Example:

POST /books

PUT

Update existing data

Example:

PUT /books/1

DELETE

Delete data

Example:

DELETE /books/1

---

## What is Stateless?

Stateless means:

Server does not remember previous requests automatically.

Each request should contain all required information.

Example:

POST /transfer

Headers:

Authorization: Bearer xyz123

Body:

Amount: 1000

The server can process request using only current request information.

Server should not depend on memory from previous requests.

---

## Why Stateless?

Makes scaling easier.

Example:

Request1 → Server A

Request2 → Server B

Request3 → Server C

Because request carries all information, any server can process it.

Useful for:

- Microservices
- Load balancers
- Distributed systems

---

## Why not frontend directly access DB?

Reasons:

### Security

Anyone could manipulate database directly.

---

### Business logic centralization

Backend handles:

- authentication
- validation
- permissions
- transaction rules
- auditing

---

### Control and scalability

Backend maintains consistency and controls access.

---

## Interview Answer

REST is a standard approach for building APIs where resources are represented using URLs and manipulated using HTTP methods while keeping communication stateless.

---

## Common Interview Questions

Q: REST vs SOAP?

Q: What is stateless?

Q: GET vs POST?

Q: PUT vs PATCH?

Q: Why use APIs?

Q: Why not allow direct DB access?