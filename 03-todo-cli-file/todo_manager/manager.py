import pickle
import uuid
from enum import Enum

class TodoStatus(Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"


class Todo:
    def __init__(self, *, id_: str, title: str, content: str, status: str):
        self.id_ = id_
        self.title = title
        self.content = content
        self.status = status

    def __str__(self):
        return f"{self.id_} {self.title}: {self.content} ({self.status})"


class TodoManager:
    def __init__(self):
        self.todo_list: dict[str, Todo] = {}
        self._file_path = "./todo-list.txt"
        self.load_from_file()

    def gen_id(self):
        return str(uuid.uuid4())
    
    def write_to_file(self):
        with open(self._file_path, "wb") as f:
            pickle.dump(self.todo_list, f)

    def load_from_file(self):
        try:
            with open(self._file_path, "rb") as f:
                todo_list = pickle.load(f)
                self.todo_list = todo_list
        except FileNotFoundError:
            open(self._file_path, "w")

    def add_todo(self, title: str, content: str):
        new_id = self.gen_id()

        new_todo = Todo(
            id_=new_id,
            title=title,
            content=content,
            status=TodoStatus.IN_PROGRESS.value
        )
        self.todo_list[new_id] = new_todo
        self.write_to_file()

    def complete_todo(self, id_: str):
        if (todo := self.todo_list.get(id_)) is not None:
            todo.status = TodoStatus.COMPLETED.value
            self.write_to_file()
        else:
            print(f"There is no todo whose id is {id_}")

    def remove_todo(self, id_: str):
        if id_ in self.todo_list:
            del self.todo_list[id_]
            self.write_to_file()
        else:
            print(f"There is no todo whose id is {id_}")

    def print_todo_list(self):
        if len(self.todo_list) == 0:
            print("No Todo Here!")
            return

        print("< My Todo List >")
        for todo in self.todo_list.values():
            print(todo)
