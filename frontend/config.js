import process from 'process';

const config = {
    backendUrl: import.meta.env.VITE_BACKEND_URL || process.env.VITE_BACKEND_URL || "http://localhost:8000", // Default for local development
    // someFeatureFlag: import.meta.env.VITE_FEATURE_FLAG === 'true', // Example feature flag for future development
};

export default config;
  