from enum import Enum


class TodoStatus(Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"


class Todo:
    def __init__(self, *, id: int, title: str, content: str, status: TodoStatus):
        self.id = id
        self.title = title
        self.content = content
        self.status = status

    def __str__(self):
        return f"#{self.id} {self.title}: {self.content} ({self.status.value})"

    def get_status(self):
        return self.status
    
    def set_status(self, status: TodoStatus):
        self.status = status

    def get_id(self):
        return self.id


class TodoManager:
    def __init__(self):
        self.id_count = 0
        self.todo_list: list[Todo] = []

    def gen_id(self):
        self.id_count += 1
        return self.id_count

    def add_todo(self, title: str, content: str):
        new_todo = Todo(
            id=self.gen_id(),
            title=title,
            content=content,
            status=TodoStatus.IN_PROGRESS
        )
        self.todo_list.append(new_todo)

    def complete_todo(self, id: int):
        for todo in self.todo_list:
            if todo.get_id() == id:
                todo.set_status(TodoStatus.COMPLETED)

    def remove_todo(self, id: int):
        for todo in self.todo_list:
            if todo.get_id() == id:
                self.todo_list.remove(todo)

    def print_todo_list(self):
        if len(self.todo_list) == 0:
            print("No Todo Here!")
            return

        print("< My Todo List >")
        for todo in self.todo_list:
            print(todo)
