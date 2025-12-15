// Products API Service
import apiClient from '../client.js';

const ProductsService = {
  // Get products by ID
  async getById(id) {
    try {
      const response = await apiClient.get('/api/products'.replace('{id}', id));
      return response;
    } catch (error) {
      console.error('Error fetching products:', error);
      throw error;
    }
  }
  // Get products by ID
  async getById(id) {
    try {
      const response = await apiClient.get('/api/products/{product_id}'.replace('{id}', id));
      return response;
    } catch (error) {
      console.error('Error fetching products:', error);
      throw error;
    }
  }
};

export default ProductsService;
