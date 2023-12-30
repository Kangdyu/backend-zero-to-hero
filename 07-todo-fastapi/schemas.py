from constants import TodoStatus
from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    content: str


class TodoUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    status: TodoStatus | None = None


class Todo(BaseModel):
    tid: str
    title: str
    content: str
    status: TodoStatus
