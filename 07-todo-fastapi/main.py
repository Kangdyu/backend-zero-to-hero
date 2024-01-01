from typing import Generic, TypeVar

from fastapi import FastAPI, Response
from pydantic import BaseModel
from schemas import Todo, TodoCreate, TodoUpdate
from todo_manager import EmptyUpdateBodyException, NotFoundException, TodoManager

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
    result = todo_manager.add_todo(todo)
    return Response(
        status_code=201, content=ResponseContent(data=result).model_dump_json()
    )


@app.patch("/todos/{tid}")
def update_todo(tid: str, todo: TodoUpdate):
    try:
        result = todo_manager.update_todo(tid=tid, todo=todo)
        return ResponseContent(data=result)
    except EmptyUpdateBodyException:
        return Response(status_code=400, content="Empty Update Body")


@app.delete("/todos/{tid}")
def delete_todo(tid: str):
    try:
        todo_manager.delete_todo(tid=tid)
        return Response(status_code=204)
    except NotFoundException:
        return Response(status_code=404, content=f"There is no todo whose id is {tid}")
