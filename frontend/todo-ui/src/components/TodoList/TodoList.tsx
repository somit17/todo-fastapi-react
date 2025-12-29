import React, { useEffect, useState } from 'react'
import { getAllTodos } from '../../api/todo.api'
import { DataTable } from 'primereact/datatable'
import { Column } from 'primereact/column'
function TodoList() {
  const [todos, setTodos] = useState()
  const cols = [
    { field: 'id', header: 'ID' },
    { field: 'title', header: 'Title' },
  ]
  useEffect(() => {
    const fetchTodos = async () => {
      const todos = await getAllTodos();
      setTodos(todos)
      console.log(todos)
    }
    fetchTodos()
  }, [])

  return (
    <DataTable value={todos}>
      {cols.map((col, i) => (
        <Column key={col.field} field={col.field} />
      ))}
    </DataTable>
  )
}

export default TodoList