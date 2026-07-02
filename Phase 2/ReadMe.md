# Phase 2 – Public Key Infrastructure (PKI)

## Overview

The second phase implements a simplified Public Key Infrastructure (PKI) to demonstrate how public-key cryptography is used in secure communication.

The project combines RSA, DSA, certificate management, and socket programming to simulate a basic certificate authority and secure client/server communication.

## Features

### Prime Number Generation

* Random large prime generation
* Miller–Rabin probabilistic primality test

### RSA

* Public key generation
* Private key generation
* PEM file export

### DSA

* CA signing key generation
* Digital signature creation
* Signature verification

### Certificate Authority

* Certificate Signing Request (CSR)
* Certificate generation
* Certificate signing
* Certificate validation

### Secure Communication

The project simulates a complete authentication process:

1. Client generates RSA keys.
2. Client creates a certificate signing request.
3. Certificate Authority signs the request.
4. Client receives a certificate.
5. Client connects to the server.
6. Server verifies the client's certificate.
7. Server generates a symmetric session key.
8. The session key is encrypted using the client's RSA public key.
9. The client decrypts the session key.
10. Encrypted communication is established using symmetric encryption.

## Technologies

* Python
* Socket Programming
* JSON
* Hashlib

## Files

```
crypto_project_second_phase.py
```

## Educational Purpose

This project demonstrates the basic workflow of a PKI system, including certificate issuance, identity verification, hybrid encryption, and secure communication. It is intended for learning cryptographic concepts rather than production use.
