# SMTP-Hammer  
[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)
![Repo Size](https://img.shields.io/github/repo-size/datareccer/SMTP-Hammer**A lightweight tool for penetration testing SMTP credentials through ethical brute-force auditing.**

> *"Truth demands clarity. Research demands honesty. There is no wrong way to seek what is right."*  
> — Wesley Middleton

---

## Overview

SMTP-Hammer is an ethical hacking tool designed to test the strength and integrity of email SMTP logins — particularly Gmail — by simulating brute-force attacks using a user-supplied password list. It is intended strictly for **authorized auditing, red teaming, or educational penetration testing scenarios.**

---

## Features

- Multi-threaded brute-force attack engine
- Supports Gmail’s SMTP server (smtp.gmail.com:587)
- Custom email/username targeting
- Color-coded status output for easy readability
- Built-in logging of attempts for documentation and compliance
- Clean and modular Python codebase

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/datareccer/SMTP-Hammer.git
cd SMTP-Hammer

2. Install dependencies:
bash
pip install -r requirements.txt

