from datetime import datetime
class Task:
    def __init__(self, title, description, deadline=None):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False
        self.assigned_to = None
        self.created_at = datetime.now()

    def mark_complete(self):
        self.completed = True
        print(f"Task '{self.title}' marked as completed.")

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        assigned = self.assigned_to if self.assigned_to else "Unassigned"
        return f"[{status}] {self.title} (Assigned to: {assigned})"










class Member:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def assign_task(self, task):
        task.assigned_to = self.name
        self.tasks.append(task)
        print(f"Task '{task.title}' assigned to {self.name}.")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                return
        print(f"No task found with title '{title}' for {self.name}.")

    def show_tasks(self):
        print(f"\nTasks for {self.name}:")
        if not self.tasks:
            print("  (No tasks assigned)")
        for task in self.tasks:
            print(f"  - {task}")













class TaskManager:
    def __init__(self):
        self.members = []
        self.tasks = []

    def add_member(self, name):
        self.members.append(Member(name))
        print(f"Added member: {name}")

    def add_task(self, title, description, deadline=None):
        self.tasks.append(Task(title, description, deadline))
        print(f"Added new task: {title}")

    def assign_task(self, task_title, member_name):
        task = None
        member = None

        # Find the task
        for t in self.tasks:
            if t.title.lower() == task_title.lower():
                task = t
                break

        # Find the member
        for m in self.members:
            if m.name.lower() == member_name.lower():
                member = m
                break

        if task is None:
            print(f"Task '{task_title}' not found.")
            return
        if member is None:
            print(f"Member '{member_name}' not found.")
            return

        member.assign_task(task)

    def complete_task(self, member_name, task_title):
        for member in self.members:
            if member.name.lower() == member_name.lower():
                member.complete_task(task_title)
                return
        print(f"Member '{member_name}' not found.")

    def show_all_tasks(self):
        print("\nAll Tasks:")
        if not self.tasks:
            print("  (No tasks yet)")
        for task in self.tasks:
            print(f"  - {task}")

    def show_members(self):
        print("\nMembers:")
        if not self.members:
            print("  (No members yet)")
        for member in self.members:
            print(f"  - {member.name}")























# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    manager = TaskManager()

    # Add members
    manager.add_member("Alice")
    manager.add_member("Bob")

    # Add tasks
    manager.add_task("Clean Kitchen", "Deep clean the kitchen.")
    manager.add_task("Water Plants", "Water all indoor plants.")
    manager.add_task("Take out Trash", "Take the trash out before 8 AM.")

    # Assign tasks
    manager.assign_task("Clean Kitchen", "Alice")
    manager.assign_task("Take out Trash", "Bob")

    # Show members and tasks
    manager.show_members()
    manager.show_all_tasks()

    # Complete a task
    manager.complete_task("Alice", "Clean Kitchen")

    # Show updated list
    manager.show_all_tasks()
