# API Connection Documentation

## Overview
This document describes the API connections between frontend and backend.

## Backend Endpoints

Total endpoints: 8

### Endpoints List

- **POST** `/api/register`
  - Function: `register`
  - Operation: `CREATE`

- **POST** `/login`
  - Function: `login`
  - Operation: `CREATE`

- **GET** `/api/products`
  - Function: `get_products`
  - Operation: `READ_ONE`

- **GET** `/api/products/{product_id}`
  - Function: `get_product`
  - Operation: `READ_ONE`

- **POST** `/api/cart`
  - Function: `add_to_cart`
  - Operation: `CREATE`

- **GET** `/api/orders`
  - Function: `get_orders`
  - Operation: `READ_ONE`

- **GET** `/api/orders/{order_id}`
  - Function: `get_order`
  - Operation: `READ_ONE`

- **POST** `/api/payments`
  - Function: `make_payment`
  - Operation: `CREATE`


## Frontend API Services

Total services: 7

### Available Services

- `register_service.js` - Register API operations
- `login_service.js` - Login API operations
- `products_service.js` - Products API operations
- `cart_service.js` - Cart API operations
- `orders_service.js` - Orders API operations
- `payments_service.js` - Payments API operations

## Usage Example

```javascript
import UserService from './api/services/user_service.js';

// Get all users
const users = await UserService.getAll();

// Get user by ID
const user = await UserService.getById(1);

// Create new user
const newUser = await UserService.create({ name: 'John', email: 'john@example.com' });

// Update user
const updated = await UserService.update(1, { name: 'Jane' });

// Delete user
await UserService.delete(1);
```

## Environment Variables

Make sure to set the following environment variables:

- `VITE_API_BASE_URL` (Vite projects)
- `NEXT_PUBLIC_API_BASE_URL` (Next.js projects)
- `REACT_APP_API_BASE_URL` (Create React App)

Default: `http://localhost:8000`
