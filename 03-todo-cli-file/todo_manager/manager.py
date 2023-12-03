from enum import Enum


class TodoStatus(Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"


class Todo:
    def __init__(self, *, id_: int, title: str, content: str, status: TodoStatus):
        self.id_ = id_
        self.title = title
        self.content = content
        self.status = status

    def __str__(self):
        return f"#{self.id_} {self.title}: {self.content} ({self.status.value})"


class TodoManager:
    def __init__(self):
        self.id_count = 0
        self.todo_list: dict[int, Todo] = {}

    def gen_id(self):
        self.id_count += 1
        return self.id_count

    def add_todo(self, title: str, content: str):
        new_id = self.gen_id()

        new_todo = Todo(
            id_=new_id,
            title=title,
            content=content,
            status=TodoStatus.IN_PROGRESS
        )
        self.todo_list[new_id] = new_todo

    def complete_todo(self, id_: int):
        if id_ in self.todo_list:
            self.todo_list[id_].status = TodoStatus.COMPLETED
        else:
            print(f"There is no todo whose id is {id_}")

    def remove_todo(self, id_: int):
        if id_ in self.todo_list:
            del self.todo_list[id_]
        else:
            print(f"There is no todo whose id is {id_}")

    def print_todo_list(self):
        if len(self.todo_list) == 0:
            print("No Todo Here!")
            return

        print("< My Todo List >")
        for value in self.todo_list.values():
            print(value)
