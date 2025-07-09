import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_CONFIG, isApiConfigured, getApiUrl } from '../config/api';
import { mockGraphsData } from '../data/mockData';

const GraphsSection = () => {
  const [graphs, setGraphs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [usingMockData, setUsingMockData] = useState(false);

  useEffect(() => {
    fetchGraphs();
  }, []);

  const fetchGraphs = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Check if API is configured
      if (!isApiConfigured()) {
        // Use mock data when API is not configured
        setTimeout(() => {
          setGraphs(mockGraphsData);
          setUsingMockData(true);
          setLoading(false);
        }, 1000); // Simulate loading time
        return;
      }

      // Try to fetch from Django API
      // const apiUrl = getApiUrl(API_CONFIG.ENDPOINTS.GRAPHS);
      // const response = await axios.get(apiUrl, {
      //   timeout: 5000, // 5 second timeout
      //   headers: {
      //     'Content-Type': 'application/json',
      //   }
      // });
      
      // setGraphs(response.data);
      // setUsingMockData(false);
      
    } catch (err) {
      console.error('Error fetching graphs:', err);
      
      let errorMessage = 'Failed to fetch graphs from server';
      
      // Provide specific error messages based on error type
      if (err.code === 'ECONNABORTED') {
        errorMessage = 'Request timed out. Please check if your Django server is running.';
      } else if (err.response) {
        // Server responded with error status
        errorMessage = `Server error: ${err.response.status} - ${err.response.statusText}`;
      } else if (err.request) {
        // Request was made but no response received
        errorMessage = 'Cannot connect to Django server. Please check if the server is running and the URL is correct.';
      }
      
      setError(errorMessage);
      
      // Fallback to mock data
      setGraphs(mockGraphsData);
      setUsingMockData(true);
      
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="space-y-6">
        <div className="flex justify-between items-center">
          <div className="h-8 bg-gray-200 rounded w-1/4 animate-pulse"></div>
          <div className="h-10 bg-gray-200 rounded w-32 animate-pulse"></div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="bg-white rounded-lg shadow-md p-6 animate-pulse">
              <div className="h-6 bg-gray-200 rounded w-3/4 mb-4"></div>
              <div className="h-64 bg-gray-200 rounded"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">Analytics Dashboard</h2>
          {usingMockData && (
            <p className="text-sm text-blue-600 mt-1">
              {isApiConfigured() ? 'Using mock data (server unavailable)' : 'Using mock data (configure API in src/config/api.js)'}
            </p>
          )}
        </div>
        <button 
          onClick={fetchGraphs}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Loading...' : 'Refresh Graphs'}
        </button>
      </div>
      
      {error && (
        <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg className="h-5 w-5 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="ml-3">
              <p className="text-yellow-700 font-medium">Connection Issue</p>
              <p className="text-yellow-600 text-sm mt-1">{error}</p>
              <p className="text-yellow-600 text-sm mt-1">Showing mock data instead.</p>
            </div>
          </div>
        </div>
      )}
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
        {graphs.map((graph) => (
          <div key={graph.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
            <div className="p-4 bg-gray-50 border-b">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-lg font-semibold text-gray-800">{graph.title}</h3>
                  {graph.description && (
                    <p className="text-sm text-gray-600 mt-1">{graph.description}</p>
                  )}
                </div>
                {graph.lastUpdated && (
                  <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                    Updated: {new Date(graph.lastUpdated).toLocaleDateString()}
                  </span>
                )}
              </div>
            </div>
            <div className="p-4">
              <div className="h-64 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden">
                <img 
                  src={graph.imageUrl} 
                  alt={graph.title}
                  className="max-h-full max-w-full object-contain rounded"
                  onError={(e) => {
                    e.target.src = 'https://images.pexels.com/photos/590016/pexels-photo-590016.jpeg?auto=compress&cs=tinysrgb&w=400';
                  }}
                />
              </div>
              <p className="text-sm text-gray-600 mt-3">
                {usingMockData 
                  ? 'Mock graph - replace with actual matplotlib graph from Django' 
                  : 'Graph generated from matplotlib'
                }
              </p>
            </div>
          </div>
        ))}
      </div>
      
      {graphs.length === 0 && !loading && (
        <div className="text-center py-12">
          <p className="text-gray-500 text-lg">No graphs available</p>
        </div>
      )}
    </div>
  );
};

export default GraphsSection;