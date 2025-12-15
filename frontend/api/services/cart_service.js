// Cart API Service
import apiClient from '../client.js';

const CartService = {
  // Create new cart
  async create(data) {
    try {
      const response = await apiClient.post('/api/cart', data);
      return response;
    } catch (error) {
      console.error('Error creating cart:', error);
      throw error;
    }
  }
};

export default CartService;
