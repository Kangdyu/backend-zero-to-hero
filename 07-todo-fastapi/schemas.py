from constants import TodoStatus
from pydantic import BaseModel, model_validator


class EmptyUpdateBodyException(Exception):
    pass


class TodoCreate(BaseModel):
    title: str
    content: str


class TodoUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    status: TodoStatus | None = None

    @model_validator(mode="after")
    def check_body_is_not_all_none(self) -> "TodoUpdate":
        if all(value is None for value in self.model_dump().values()):
            raise EmptyUpdateBodyException
        else:
            return self


class Todo(BaseModel):
    tid: str
    title: str
    content: str
    status: TodoStatus
