# Secure Flask CRUD Application

A simple Flask contact management application implementing OWASP security best practices.

## Security Features

1. **Secure Input Handling** - Custom validators to prevent SQL Injection and XSS attacks
2. **Parameterized Queries** - SQLAlchemy ORM for safe database operations
3. **CSRF Protection** - Flask-WTF tokens on all forms
4. **Secure Session Management** - HttpOnly cookies, SameSite protection, session timeout
5. **Secure Error Handling** - Custom error pages preventing information disclosure
6. **Secure Password Storage** - Bcrypt hashing with unique salts

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access at: http://localhost:5000

## Usage

1. Register a new account
2. Login with your credentials
3. Add, view, and delete contacts
4. Logout when done
