# Lab 9: Codacy Setup Guide

## What is Codacy?
Codacy is an automated code review tool that analyzes your code for:
- Security issues
- Code quality
- Code coverage
- Complexity
- Duplication

## Setup Steps

### 1. Access Codacy
1. Go to https://www.codacy.com/
2. Click "Sign up with GitHub"
3. Authorize Codacy to access your GitHub repositories

### 2. Add Your Repository
1. Once logged in, click "Add repository"
2. Find `hello-jenkins-demo` in the list
3. Click "Add to Codacy"

### 3. Wait for Analysis
- Codacy will automatically analyze your code
- This usually takes 2-5 minutes for the first scan
- You'll see a dashboard with results

### 4. Review Results
The dashboard will show:
- **Overall Grade**: A-F rating
- **Issues**: Security, Error Prone, Code Style, Complexity
- **Security**: Vulnerability detection
- **Duplication**: Code duplication percentage
- **Complexity**: Cyclomatic complexity metrics

## Expected Results for Our App

### Security Issues
✓ Should find minimal/no critical security issues because we implemented:
- SQL Injection prevention (SQLAlchemy ORM)
- XSS prevention (input validators)
- CSRF protection (Flask-WTF)
- Secure password storage (Bcrypt)
- Secure session management
- Custom error handling

### Code Quality
May report:
- Missing docstrings (minor)
- Line length issues (minor)
- Complexity warnings (if any function is too complex)

### Files Analyzed
- `app.py` - Main application
- `models.py` - Database models
- `forms.py` - Form validators
- `run_static_analysis.py` - Static analysis script
- `run_dynamic_analysis.py` - Dynamic analysis script

## Understanding the Dashboard

### 1. Issues Tab
- Lists all detected issues by category
- Click on any issue to see details and fix suggestions

### 2. Security Tab
- Shows security vulnerabilities
- Categorized by severity (Critical, Warning, Info)

### 3. Files Tab
- Shows code quality per file
- Grade (A-F) for each file

### 4. Settings Tab
- Configure which tools to run
- Exclude files/patterns
- Set coding standards

## Screenshot Checklist for Lab Report

1. ✓ Codacy Dashboard (overall grade)
2. ✓ Security issues tab (should show minimal issues)
3. ✓ Code quality metrics
4. ✓ Individual file analysis (app.py, forms.py, models.py)
5. ✓ Complexity metrics
6. ✓ Configuration settings (.codacy.yml)

## Comparison with Local Analysis

### Local Tools (Already Run)
- Bandit - Security analysis
- Flake8 - Style guide
- Pylint - Code quality

### Codacy (Cloud-based)
- Combines multiple tools
- Historical tracking
- PR integration
- Team collaboration

## Repository URL
https://github.com/Areej-zeb/hello-jenkins-demo

## Next Steps
1. Log into Codacy with GitHub
2. Add the repository
3. Wait for analysis
4. Take screenshots of results
5. Compare with local static analysis results
6. Document findings in lab report

## Tips
- Fix critical issues first
- Ignore minor style issues if they don't affect security
- Use Codacy badges in README (optional)
- Set up PR checks for future commits (optional)
