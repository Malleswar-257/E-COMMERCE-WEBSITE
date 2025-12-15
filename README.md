# E-COMMERCE-WEBSITE

Backend generation request for repo https://github.com/Malleswar-249/E-COMMERCE-WEBSITE

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy
- **Frontend**: Provided via GitHub repo (https://github.com/Malleswar-249/E-COMMERCE-WEBSITE)

## Project Structure

```
E-COMMERCE-WEBSITE/
├── frontend/           # Frontend (cloned from provided repo)
├── backend/            # Backend API
├── README.md           # This file
└── docker-compose.yml  # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)
- Node.js 18+ (for frontend from repo)

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
python -m venv .venv
source .venv/bin/activate  # or .venv\Scriptsctivate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup (from provided repo)

```bash
cd frontend
npm install
npm run dev
```

## Features

- user registration
- user login
- product browsing
- cart management
- checkout and payment

## API Endpoints

- `POST /api/register` - Register a new user account
- `POST /api/login` - Login to an existing user account
- `GET /api/products` - Get a list of all products
- `GET /api/products/{category}` - Get a list of products by category
- `POST /api/cart` - Add a product to the cart
- `POST /api/checkout` - Checkout and make a payment

## License

MIT
