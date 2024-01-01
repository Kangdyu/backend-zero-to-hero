from enum import Enum


class TodoStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"
