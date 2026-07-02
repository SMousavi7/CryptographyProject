# Cryptography Course Project

This repository contains the implementation of a two-phase course project for the **Introduction to Cryptography** course.

The project covers both **symmetric cryptography** and **public key infrastructure (PKI)** concepts. All implementations were developed in Python for educational purposes without relying on high-level cryptographic libraries for the core algorithms.

## Project Structure

```
.
├── crypto_project_first_phase.py
├── crypto_project_second_phase.py
├── گزارش پروژه‌ی رمزنگاری فاز۱.pdf
└── گزارش پروژه‌ی رمزنگاری فاز۲.pdf
```

## Phase 1 – Symmetric Cryptography

The first phase focuses on implementing a custom block cipher based on the specification provided in the course.

Implemented components include:

* S-Box implementation
* Round function
* Key scheduling
* 128-bit key management
* Generation of round keys
* Encryption
* Decryption
* Multiple block cipher modes:

  * ECB
  * CBC
  * CTR
  * OFB

The implementation also includes helper utilities for binary operations, conversions, padding, XOR operations and block processing.

---

## Phase 2 – Public Key Infrastructure (PKI)

The second phase extends the project toward public-key cryptography by implementing a simplified PKI workflow.

Implemented components include:

* Large prime generation
* Miller–Rabin primality testing
* RSA key generation
* DSA key generation
* PEM key export
* Certificate Signing Request (CSR)
* Certificate Authority (CA)
* Certificate signing
* Certificate verification
* Secure client/server communication
* Hybrid encryption using asymmetric and symmetric cryptography
* Socket-based communication

---

## Reports

Two detailed reports are included:

* Phase 1 Report
* Phase 2 Report

These reports explain the implementation details, design decisions, and important parts of the code.

## Technologies

* Python
* NumPy
* Socket Programming
* JSON
* Hashlib

## Educational Purpose

This repository was developed as a university project for learning and understanding cryptographic algorithms and PKI concepts. The implementation is intended for educational use and should **not** be used in production environments.
