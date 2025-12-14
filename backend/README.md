# E-COMMERCE-WEBSITE

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create a new PostgreSQL database and update `.env.example` with your credentials
3. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints
* `/api/register`: Register a new user
* `/api/login`: Login a user
* `/api/products`: Get all products
* `/api/products/{id}`: Get a product by ID
* `/api/cart`: Add an item to cart
* `/api/cart`: Get cart items
* `/api/checkout`: Complete secure checkout
* `/api/orders`: Get all orders
* `/api/orders/{id}`: Get an order by ID
