import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const submitFeedback = async (feedback) => {
  const response = await api.post('/feedback/', feedback);
  return response.data;
};
