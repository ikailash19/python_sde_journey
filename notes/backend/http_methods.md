# HTTP Methods & Password Security

Status: Learning
Last Revised: 03-Jun-2026

Interview Confidence:
⭐

## What is HTTP?

HTTP (HyperText Transfer Protocol) is a communication protocol used between clients and servers.

Example:

Browser / Mobile App
↓
HTTP Request
↓
Backend Server
↓
HTTP Response
↓
Browser / Mobile App

---

## GET

Purpose:

Retrieve data from server.

Examples:

GET /users

GET /books

GET /movies

Characteristics:

- Used for reading data
- Should not modify data
- Can be called multiple times safely

Example:

GET /users/1

Response:

{
    "id": 1,
    "name": "Kailash"
}

---

## POST

Purpose:

Create new data on server.

Examples:

POST /users

POST /books

POST /orders

Characteristics:

- Creates resources
- Usually changes server state

Example:

POST /users

Request Body:

{
    "name": "Kailash"
}

Response:

{
    "id": 1,
    "name": "Kailash"
}

---

## PUT

Purpose:

Replace an entire resource.

Example:

Current User:

{
    "name": "Kailash",
    "age": 29,
    "city": "Chennai"
}

PUT /users/1

{
    "name": "Kailash",
    "age": 30,
    "city": "Chennai"
}

Result:

Entire record is replaced.

Think:

Replace everything.

---

## PATCH

Purpose:

Update specific fields only.

Example:

PATCH /users/1

{
    "age": 30
}

Result:

Only age changes.

Think:

Partial update.

---

## PUT vs PATCH

PUT:

- Replaces complete resource

PATCH:

- Updates selected fields only

Interview Answer:

PUT replaces the entire resource while PATCH updates only specific fields.

---

## Common HTTP Status Codes

200 OK

Request successful.

201 Created

Resource created successfully.

400 Bad Request

Invalid request from client.

401 Unauthorized

Authentication required.

403 Forbidden

User authenticated but not allowed.

404 Not Found

Resource does not exist.

500 Internal Server Error

Server-side failure.

---

## Why Not Store Passwords in Plain Text?

Wrong:

Database:

username: kailash
password: mypassword123

If database leaks, attackers get actual passwords.

---

## Password Hashing

Passwords should be hashed before storing.

Example:

mypassword123

↓

bcrypt hash

↓

$2b$12$xyz...

Stored in database:

username: kailash
password_hash: $2b$12$xyz...

---

## Hashing vs Encryption

Hashing:

- One-way process
- Cannot easily recover original password
- Used for passwords

Examples:

- bcrypt
- Argon2
- scrypt

Encryption:

- Can be decrypted
- Used for sensitive data transmission/storage

Examples:

- AES
- RSA

---

## Login Flow

User enters password

↓

Password hashed

↓

Compare hash with database hash

↓

If hashes match:

Login Success

Else:

Login Failed

---

## Interview Questions

Q: What is HTTP?

Q: GET vs POST?

Q: PUT vs PATCH?

Q: Why should GET not modify data?

Q: What is a 404 error?

Q: What is password hashing?

Q: Hashing vs Encryption?

Q: Why should passwords not be stored in plain text?