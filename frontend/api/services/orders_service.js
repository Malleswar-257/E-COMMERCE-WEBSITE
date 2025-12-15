// Orders API Service
import apiClient from '../client.js';

const OrdersService = {
  // Get orders by ID
  async getById(id) {
    try {
      const response = await apiClient.get('/api/orders'.replace('{id}', id));
      return response;
    } catch (error) {
      console.error('Error fetching orders:', error);
      throw error;
    }
  }
  // Get orders by ID
  async getById(id) {
    try {
      const response = await apiClient.get('/api/orders/{order_id}'.replace('{id}', id));
      return response;
    } catch (error) {
      console.error('Error fetching orders:', error);
      throw error;
    }
  }
};

export default OrdersService;
