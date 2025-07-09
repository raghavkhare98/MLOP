// API Configuration
// Replace this URL with your Django server URL when ready
export const API_CONFIG = {
  // Set this to your Django server URL (e.g., 'http://localhost:8000' or 'https://your-django-server.com')
  BASE_URL: '', // Leave empty to use mock data
  
  // API endpoints
  ENDPOINTS: {
    DATA: '/api/data/',
    GRAPHS: '/api/graphs/',
  }
};

// Helper function to check if API is configured
export const isApiConfigured = () => {
  return API_CONFIG.BASE_URL && API_CONFIG.BASE_URL.trim() !== '';
};

// Helper function to get full API URL
export const getApiUrl = (endpoint) => {
  if (!isApiConfigured()) {
    return null;
  }
  return `${API_CONFIG.BASE_URL}${endpoint}`;
};