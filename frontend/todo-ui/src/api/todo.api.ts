import axios from "axios";

const API_URL = import.meta.env.VITE_API_BASE_URL;

export  const getAllTodos = async ()=>{
  const response = await axios.get(`${API_URL}/todos`);
  return response.data;
} 