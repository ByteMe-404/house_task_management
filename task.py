from datetime import datetime

class Task:
    def _init_(self, name, difficulty, deadline):
        self.name = name
        self.difficulty = difficulty
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"

    def is_overdue(self):
        return datetime.now() > self.deadline and self.status != "Completed"

    def to_dict(self):
        return {
            "name": self.name,
            "difficulty": self.difficulty,
            "deadline": self.deadline.strftime("%Y-%m-%d"),
            "status": self.status
        }
    
