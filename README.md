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

- Product management
- User authentication
- Order handling
- Payment processing

## API Endpoints

- `GET /api/products` - Retrieve a list of products available for purchase.
- `GET /api/cart/{user_id}` - Retrieve the shopping cart for a specific user.
- `POST /api/orders` - Place a new order.
- `POST /api/login` - User login to access account features.
- `POST /api/register` - User registration for a new account.

## License

MIT
