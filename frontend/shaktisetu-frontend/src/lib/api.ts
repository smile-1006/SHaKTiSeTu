// API client for ShaktiSetu backend
const API_BASE_URL = 'http://localhost:5000/api';

// Interface for API response
interface ApiResponse<T> {
  data?: T;
  error?: string;
}

// Generic fetch function with error handling
async function fetchApi<T>(
  endpoint: string, 
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  try {
    const url = `${API_BASE_URL}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    const response = await fetch(url, { ...options, headers });
    const data = await response.json();

    if (!response.ok) {
      return { error: data.error || 'An error occurred' };
    }

    return { data: data as T };
  } catch (error) {
    return { error: (error as Error).message };
  }
}

// Auth API
export const authApi = {
  login: async (email: string, password: string) => {
    return fetchApi('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  },
  register: async (userData: any) => {
    return fetchApi('/auth/register', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  },
  getProfile: async (token: string) => {
    return fetchApi('/auth/profile', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

// User API
export const userApi = {
  getUsers: async (token: string) => {
    return fetchApi('/users', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  getUser: async (userId: number, token: string) => {
    return fetchApi(`/users/${userId}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  updateUser: async (userId: number, userData: any, token: string) => {
    return fetchApi(`/users/${userId}`, {
      method: 'PUT',
      body: JSON.stringify(userData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

// Marketplace API
export const marketplaceApi = {
  getProducts: async () => {
    return fetchApi('/marketplace/products');
  },
  getProduct: async (productId: number) => {
    return fetchApi(`/marketplace/products/${productId}`);
  },
  createProduct: async (productData: any, token: string) => {
    return fetchApi('/marketplace/products', {
      method: 'POST',
      body: JSON.stringify(productData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  updateProduct: async (productId: number, productData: any, token: string) => {
    return fetchApi(`/marketplace/products/${productId}`, {
      method: 'PUT',
      body: JSON.stringify(productData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  getRecommendations: async (userId: number) => {
    return fetchApi(`/marketplace/recommendations/${userId}`);
  },
};

// Storefront API
export const storefrontApi = {
  getStorefronts: async () => {
    return fetchApi('/storefronts');
  },
  getStorefront: async (storefrontId: number) => {
    return fetchApi(`/storefronts/${storefrontId}`);
  },
  createStorefront: async (storefrontData: any, token: string) => {
    return fetchApi('/storefronts', {
      method: 'POST',
      body: JSON.stringify(storefrontData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  getSections: async (storefrontId: number) => {
    return fetchApi(`/storefronts/${storefrontId}/sections`);
  },
  createSection: async (storefrontId: number, sectionData: any, token: string) => {
    return fetchApi(`/storefronts/${storefrontId}/sections`, {
      method: 'POST',
      body: JSON.stringify(sectionData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

// Learning API
export const learningApi = {
  getCourses: async () => {
    return fetchApi('/learning/courses');
  },
  getCourse: async (courseId: number) => {
    return fetchApi(`/learning/courses/${courseId}`);
  },
  getModules: async (courseId: number) => {
    return fetchApi(`/learning/courses/${courseId}/modules`);
  },
  getLessons: async (moduleId: number) => {
    return fetchApi(`/learning/modules/${moduleId}/lessons`);
  },
  updateProgress: async (userId: number, lessonId: number, progressData: any, token: string) => {
    return fetchApi(`/learning/users/${userId}/progress/${lessonId}`, {
      method: 'POST',
      body: JSON.stringify(progressData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

// Government Schemes API
export const governmentApi = {
  getSchemes: async () => {
    return fetchApi('/government/schemes');
  },
  getScheme: async (schemeId: number) => {
    return fetchApi(`/government/schemes/${schemeId}`);
  },
  checkEligibility: async (userId: number, schemeId: number, token: string) => {
    return fetchApi('/government/schemes/check-eligibility', {
      method: 'POST',
      body: JSON.stringify({ user_id: userId, scheme_id: schemeId }),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  applyForScheme: async (schemeId: number, applicationData: any, token: string) => {
    return fetchApi(`/government/schemes/${schemeId}/applications`, {
      method: 'POST',
      body: JSON.stringify(applicationData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

// Mentorship API
export const mentorshipApi = {
  getMentors: async () => {
    return fetchApi('/mentorship/mentors');
  },
  getMentor: async (mentorId: number) => {
    return fetchApi(`/mentorship/mentors/${mentorId}`);
  },
  bookSession: async (sessionData: any, token: string) => {
    return fetchApi('/mentorship/sessions', {
      method: 'POST',
      body: JSON.stringify(sessionData),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
  getPeerGroups: async () => {
    return fetchApi('/mentorship/peer-groups');
  },
  joinGroup: async (groupId: number, userId: number, token: string) => {
    return fetchApi(`/mentorship/peer-groups/${groupId}/join`, {
      method: 'POST',
      body: JSON.stringify({ user_id: userId }),
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  },
};

export default {
  auth: authApi,
  users: userApi,
  marketplace: marketplaceApi,
  storefront: storefrontApi,
  learning: learningApi,
  government: governmentApi,
  mentorship: mentorshipApi,
};
