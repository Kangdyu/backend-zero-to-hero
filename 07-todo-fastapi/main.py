from typing import Generic, TypeVar

from fastapi import FastAPI, Response
from pydantic import BaseModel
from schemas import Todo, TodoCreate, TodoUpdate
from todo_manager import TodoManager

app = FastAPI()
todo_manager = TodoManager()

DataT = TypeVar("DataT")


class ResponseContent(BaseModel, Generic[DataT]):
    data: DataT


@app.get("/todos")
def get_todo_list() -> ResponseContent[list[Todo]]:
    todo_list = todo_manager.get_todo_list()
    return ResponseContent(data=todo_list)


@app.post("/todos")
def add_todo(todo: TodoCreate):
    todo_manager.add_todo(todo)
    return Response(status_code=201)


@app.patch("/todos/{tid}")
def update_todo(tid: str, todo: TodoUpdate):
    todo_manager.update_todo(tid=tid, todo=todo)
    return Response(status_code=204)


@app.delete("/todos/{tid}")
def delete_todo(tid: str):
    todo_manager.delete_todo(tid=tid)
    return Response(status_code=204)
