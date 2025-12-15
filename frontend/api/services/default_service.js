// Default API Service
import apiClient from '../client.js';

const DefaultService = {
  // Get default by ID
  async getById(id) {
    try {
      const response = await apiClient.get('/'.replace('{id}', id));
      return response;
    } catch (error) {
      console.error('Error fetching default:', error);
      throw error;
    }
  }
};

export default DefaultService;
