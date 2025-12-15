// Payments API Service
import apiClient from '../client.js';

const PaymentsService = {
  // Create new payments
  async create(data) {
    try {
      const response = await apiClient.post('/api/payments', data);
      return response;
    } catch (error) {
      console.error('Error creating payments:', error);
      throw error;
    }
  }
};

export default PaymentsService;
