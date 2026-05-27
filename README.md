# Amazon Automation Testing

End-to-end test suite for Amazon.com built with Playwright and Python.

## Tech Stack
- Python 3.12
- Playwright
- Pytest

## Setup
```bash
pip install -r requirements.txt
playwright install
```

## Run Tests
```bash
pytest tests/
```

## Test Coverage
- Login
- Search
- Add to Cart
- Checkout

## Environment Variables
Create a `.env` file in the root folder:
```
AMAZON_EMAIL=your_email
AMAZON_PASSWORD=your_password
AMAZON_USERNAME=your_name
```