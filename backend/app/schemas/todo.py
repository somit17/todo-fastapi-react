import datetime
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    title:str
    description:Optional[str]=None

class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    is_completed=Optional[bool]=None


class TodoResponse(TodoBase):
    id: int
    is_completed: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2