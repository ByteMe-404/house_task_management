from datetime import datetime

class Task:
    def __init__(self, name, difficulty, deadline):
        self.name = name
        self.difficulty = difficulty
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"

    def is_overdue(self):
        return datetime.now() > self.deadline and self.status != "Completed"

    def __str__(self):
        return f"{self.name} ({self.difficulty}) - {self.status}, Deadline: {self.deadline.strftime('%Y-%m-%d')}"


