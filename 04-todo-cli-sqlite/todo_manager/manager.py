import sqlite3
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
        self.connection = sqlite3.connect("todo-list.db")
        self.cursor = self.connection.cursor()
        self.init_db_table()

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        self.connection.close()

    def gen_id(self):
        return str(uuid.uuid4())
    
    def init_db_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS todos (id TEXT PRIMARY KEY, title TEXT, content TEXT, status TEXT)"
        )
        self.connection.commit()

    def add_todo(self, title: str, content: str):
        new_id = self.gen_id()
        self.cursor.execute(
            "INSERT INTO todos VALUES (:id, :title, :content, :status)",
            {"id": new_id, "title": title, "content": content, "status": TodoStatus.IN_PROGRESS.value}
        )
        self.connection.commit()

    def complete_todo(self, id_: str):
        self.cursor.execute(
            "UPDATE todos SET status=:status WHERE id=:id", 
            {"id": id_, "status": TodoStatus.COMPLETED.value}
        )
        self.connection.commit()

    def remove_todo(self, id_: str):
        self.cursor.execute(
            "DELETE FROM todos WHERE id=:id",
            {"id": id_}
        )
        self.connection.commit()

    def print_todo_list(self):
        todo_list = self.cursor.execute("SELECT * FROM todos").fetchall()
        if len(todo_list) == 0:
            print("No Todo Here!")
            return
        
        print("< My Todo List >")
        for (id_, title, content, status) in todo_list:
            print(Todo(id_=id_, title=title, content=content, status=status))
