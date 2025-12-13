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

- User registration and login
- Product browsing
- Cart management
- Admin product management

## API Endpoints

- `POST /api/register` - Endpoint for user registration
- `POST /api/login` - Endpoint for user login
- `GET /api/products` - Endpoint for browsing products
- `POST /api/cart/add` - Endpoint for adding items to the cart
- `GET /api/admin/products` - Endpoint for admin to manage products

## License

MIT
