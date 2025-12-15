// Register API Service
import apiClient from '../client.js';

const RegisterService = {
  // Create new register
  async create(data) {
    try {
      const response = await apiClient.post('/register', data);
      return response;
    } catch (error) {
      console.error('Error creating register:', error);
      throw error;
    }
  }
};

export default RegisterService;
