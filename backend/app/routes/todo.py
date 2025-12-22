from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import TodoCreate,TodoResponse,TodoUpdate
from app.models import ToDo
from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.get(path="/",response_model=List[TodoResponse],status_code=status.HTTP_200_OK)
def get_all_todo(db:Session=Depends(get_db)):
    all_todo = db.query(ToDo).all()
    return all_todo


@router.post(
    "/",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    new_todo = ToDo(
        title=todo.title,
        description=todo.description
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.put(path="/{todo_id}",response_model=TodoResponse,status_code=status.HTTP_200_OK)
def update_todo(todo_id:int,todo_update:TodoUpdate,db:Session=Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found")
    if todo_update.title is not None:
        todo.title = todo_update.title
    if  todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.is_completed is not None:
        todo.is_completed = todo_update.is_completed

    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id==todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found")
    else:
        db.delete(todo)
        db.commit()




