import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authApi = {
  register: (data: any) => apiClient.post('/users/register', data),
  login: (data: any) => apiClient.post('/users/login', data),
  getCurrentUser: () => apiClient.get('/users/me'),
};

export const catsApi = {
  list: () => apiClient.get('/cats'),
  create: (data: any) => apiClient.post('/cats', data),
  get: (id: string) => apiClient.get(`/cats/${id}`),
  update: (id: string, data: any) => apiClient.put(`/cats/${id}`, data),
  delete: (id: string) => apiClient.delete(`/cats/${id}`),
};

export const healthApi = {
  list: (catId: string) => apiClient.get(`/cats/${catId}/health`),
  create: (catId: string, data: any) => apiClient.post(`/cats/${catId}/health`, data),
  get: (catId: string, recordId: string) => apiClient.get(`/cats/${catId}/health/${recordId}`),
  update: (catId: string, recordId: string, data: any) => apiClient.put(`/cats/${catId}/health/${recordId}`, data),
  delete: (catId: string, recordId: string) => apiClient.delete(`/cats/${catId}/health/${recordId}`),
};

export const feedingApi = {
  listLogs: (catId: string) => apiClient.get(`/cats/${catId}/feeding/logs`),
  createLog: (catId: string, data: any) => apiClient.post(`/cats/${catId}/feeding/logs`, data),
  listSchedules: (catId: string) => apiClient.get(`/cats/${catId}/feeding/schedules`),
  createSchedule: (catId: string, data: any) => apiClient.post(`/cats/${catId}/feeding/schedules`, data),
};

export const moodApi = {
  list: (catId: string) => apiClient.get(`/cats/${catId}/mood`),
  create: (catId: string, data: any) => apiClient.post(`/cats/${catId}/mood`, data),
  getAnalysis: (catId: string, days?: number) => apiClient.get(`/cats/${catId}/mood/analysis/summary`, { params: { days } }),
};

export default apiClient;