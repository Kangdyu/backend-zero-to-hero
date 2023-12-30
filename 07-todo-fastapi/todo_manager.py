import sqlite3
import uuid

from constants import TodoStatus
from exceptions import EmptyUpdateBodyException, NotFoundException
from schemas import Todo, TodoCreate, TodoUpdate


class TodoManager:
    def __init__(self):
        self.connection = sqlite3.connect("todo-list.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.init_db_table()

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        self.connection.close()

    def gen_id(self) -> str:
        return str(uuid.uuid4())

    def init_db_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS todos (id TEXT PRIMARY KEY, title TEXT, content TEXT, status TEXT)"
        )
        self.connection.commit()

    def add_todo(self, todo: TodoCreate):
        new_id = self.gen_id()
        self.cursor.execute(
            "INSERT INTO todos VALUES (:id, :title, :content, :status)",
            {
                "id": new_id,
                "title": todo.title,
                "content": todo.content,
                "status": TodoStatus.IN_PROGRESS.value,
            },
        )
        self.connection.commit()

    def update_todo(self, tid: str, todo: TodoUpdate):
        set_list: list[str] = []
        set_value_dict = {"id": tid}

        if (title := todo.title) is not None:
            set_list.append("title")
            set_value_dict["title"] = title

        if (content := todo.content) is not None:
            set_list.append("content")
            set_value_dict["content"] = content

        if (status := todo.status) is not None:
            set_list.append("status")
            set_value_dict["status"] = status.value

        if len(set_list) == 0:
            raise EmptyUpdateBodyException

        set_clause = ", ".join([f"{column} = :{column}" for column in set_list])

        query = f"UPDATE todos SET {set_clause} WHERE id = :id"

        self.cursor.execute(
            query,
            set_value_dict,
        )
        self.connection.commit()

    def delete_todo(self, tid: str):
        result = self.cursor.execute("DELETE FROM todos WHERE id=:id", {"id": tid})

        if result.rowcount == 0:
            raise NotFoundException

        self.connection.commit()

    def get_todo_list(self) -> list[Todo]:
        todo_list: list[Todo] = []

        results = self.cursor.execute("SELECT * FROM todos").fetchall()
        for tid, title, content, status in results:
            todo_list.append(Todo(tid=tid, title=title, content=content, status=status))

        return todo_list
