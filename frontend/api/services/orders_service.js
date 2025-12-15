// Orders API Service
import apiClient from '../client.js';

const OrdersService = {
  // Create new orders
  async create(data) {
    try {
      const response = await apiClient.post('/api/orders', data);
      return response;
    } catch (error) {
      console.error('Error creating orders:', error);
      throw error;
    }
  }
};

export default OrdersService;
