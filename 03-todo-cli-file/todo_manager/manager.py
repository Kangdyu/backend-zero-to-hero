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
        self._file_delimiter = "|"
        self.load_from_file()

    def gen_id(self):
        return str(uuid.uuid4())
    
    def write_to_file(self):
        with open(self._file_path, "w") as f:
            for todo in self.todo_list.values():
                f.write(self._file_delimiter.join([todo.id_, todo.title, todo.content, todo.status]) + "\n")

    def load_from_file(self):
        try:
            with open(self._file_path, "r") as f:
                todos = f.readlines()
                for todo in todos:
                    id_, title, content, status = todo.strip().split(self._file_delimiter)
                    self.todo_list[id_] = Todo(id_=id_, title=title, content=content, status=status)
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
        if id_ in self.todo_list:
            self.todo_list[id_].status = TodoStatus.COMPLETED.value
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
