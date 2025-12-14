# E-commerce Backend API

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a new PostgreSQL database and update the `DATABASE_URL` in `.env.example`
3. Run the API: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints

* `POST /api/register`: Register a new user
* `POST /api/login`: Login an existing user
* `GET /api/products`: Get all products
* `GET /api/products/{id}`: Get a product by id
* `POST /api/cart`: Add a product to the cart
* `GET /api/cart`: Get the cart
* `POST /api/checkout`: Checkout
* `GET /api/orders`: Get all orders
* `GET /api/orders/{id}`: Get an order by id