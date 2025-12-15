// Login API Service
import apiClient from '../client.js';

const LoginService = {
  // Create new login
  async create(data) {
    try {
      const response = await apiClient.post('/login', data);
      return response;
    } catch (error) {
      console.error('Error creating login:', error);
      throw error;
    }
  }
};

export default LoginService;
