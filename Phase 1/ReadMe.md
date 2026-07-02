# Phase 1 – Symmetric Cryptography

## Overview

The objective of this phase is to implement a complete symmetric encryption system based on the algorithm described in the course project specification.

Instead of using existing cryptographic libraries, the cipher was implemented from scratch in Python to better understand the internal structure of block ciphers.

## Features

* Hardcoded S-Boxes
* Binary-based internal operations
* Helper functions for binary manipulation
* Substitution using S-Boxes
* Round function implementation
* 128-bit master key support
* Round key generation
* Encryption
* Decryption

## Supported Block Cipher Modes

* ECB (Electronic Codebook)
* CBC (Cipher Block Chaining)
* CTR (Counter Mode)
* OFB (Output Feedback)

Each mode has separate encryption and decryption implementations.

## Internal Components

The implementation contains several modules responsible for:

* Binary conversion
* XOR operations
* Block processing
* Padding
* Key scheduling
* Round transformations
* Encryption pipeline
* Decryption pipeline

## Testing

The implementation was tested by encrypting plaintext messages and decrypting them back to verify correctness.

Different encryption modes were also tested independently.

## Files

```
crypto_project_first_phase.py
```

## Notes

This implementation was developed for educational purposes to demonstrate how a block cipher can be implemented from scratch without using external cryptographic frameworks.
