# COPS-CSOC

Writeups and projects from **CSOC 2024** (Cyber Security Orientation Challenge), IIT (BHU) Varanasi's introductory infosec program run by COPS Infosec. Selected as one of 7 finalists from 40+ participants.

## Structure

### Fundamentals (Week 0)
Linux basics and beginner CTF-style problem solving (Bandit wargame, scripting challenges).

### Forensics & Steganography (Week 1)
File analysis, metadata extraction, and hidden-data recovery challenges — identifying file types by signature, extracting data from images/archives, and OSINT-based challenges.

### Cryptography (Week 2)
RSA and symmetric cipher challenges (CryptoHack) — covering classic attacks like small-exponent RSA, key reuse, and block cipher mode weaknesses.

### Web Security (Week 3)
Client-side and server-side web exploitation — XSS, JWT manipulation, Burp Suite–based request tampering, and access-control bypass challenges.

### Binary Exploitation (Week 4)
Stack-based buffer overflow challenges (Stack0–Stack5), progressing from basic stack smashing to return-address overwrites and shellcode execution.

## Independent Projects

### Project 1 — Game Save File Reverse Engineering
Reverse-engineered save files for two games (*Subway Surfers*, *Raft*) by hex-editing binary save data. Identified data encoding patterns (little-endian value fields, encrypted profile data), located and modified in-game stats (health, hunger, thirst) directly via hex editor, and validated changes in-game.

### Project 2 — Vulnerable Web Application
Built a deliberately vulnerable Flask login application to demonstrate SQL injection, containerized with Docker/docker-compose. Includes a working exploit (`' or 1=1;--`) that bypasses authentication, along with setup instructions to run and test it locally.

## Tools & Techniques Used
Python, C++, Shell scripting, Docker, Burp Suite, HxD (hex editor), Flask, SQL injection, buffer overflow exploitation, RSA cryptanalysis, JWT/session manipulation.
