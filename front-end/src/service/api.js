// Import axios tu use the API
import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
    baseURL: "http://localhost:8000"
})

// Export the Axios instance (if i want to use in jsx)
//export default api; 

// Create the get route for the project
// API request to get all projects
export  const fetchProjects = async() => {
        const response = await api.get('/projects');
        console.log(response.data)
        return response.data;
    }