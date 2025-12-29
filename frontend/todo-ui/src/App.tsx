import { Button } from 'primereact/button';
import 'primereact/resources/themes/lara-light-indigo/theme.css'; //theme
import 'primereact/resources/primereact.min.css'; //core css
import 'primeicons/primeicons.css'; //icons
import './App.css';
import { useState } from 'react';
import { Card } from 'primereact/card';
import { InputText } from 'primereact/inputtext';
import TodoList from './components/TodoList/TodoList';

function App() {
  const API_URL = import.meta.env.VITE_API_BASE_URL;

  const [title, setTitle] = useState("");

  const addTodo = async () => {
    if (!title.trim()) return;

    await fetch(`${API_URL}/todos`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title }),
    });

    setTitle("");
  };
  return (
    <div className="flex justify-content-center mt-6">
      <TodoList/>
    </div>
  );
}

export default App;