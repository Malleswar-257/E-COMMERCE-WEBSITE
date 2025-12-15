# API Connection Documentation

## Overview
This document describes the API connections between frontend and backend.

## Backend Endpoints

Total endpoints: 5

### Endpoints List

- **GET** `/`
  - Function: `read_root`
  - Operation: `READ_ONE`

- **POST** `/api/register`
  - Function: `register`
  - Operation: `CREATE`

- **POST** `/api/login`
  - Function: `login`
  - Operation: `CREATE`

- **POST** `/api/cart`
  - Function: `add_to_cart`
  - Operation: `CREATE`

- **POST** `/api/orders`
  - Function: `create_order`
  - Operation: `CREATE`


## Frontend API Services

Total services: 6

### Available Services

- `default_service.js` - Default API operations
- `register_service.js` - Register API operations
- `login_service.js` - Login API operations
- `cart_service.js` - Cart API operations
- `orders_service.js` - Orders API operations

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
