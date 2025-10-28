from member import Member
from task import Task

class TaskManager:
    def __init__(self):
        self.members = []



    def add_member(self, name, age):
        member = Member(name, age)
        self.members.append(member)
        print(f"Member '{name}' added successfully.")



    def find_member(self, name):
        for m in self.members:
            if m.name.lower() == name.lower():
                return m
        return None



    def add_task(self, name, difficulty, deadline):
        return Task(name, difficulty, deadline)



    def assign_task_to_member(self, task_name, member_name, difficulty, deadline):
        member = self.find_member(member_name)
        if not member:
            print(f" Member '{member_name}' not found.")
            return
        task = Task(task_name, difficulty, deadline)
        member.assign_task(task)



    def complete_task(self, member_name, task_name):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        member.complete_task(task_name)



    def show_member_tasks(self, member_name):
        member = self.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        member.show_tasks()



    def show_all_members(self):
        if not self.members:
            print("No members added yet.")
            return
        print("\nAll Members:")
        for m in self.members:
            print(m)


    def show_overdue_tasks(self):
        print("\nOverdue Tasks:")
        for member in self.members:
            for task in member.tasks:
                if task.is_overdue():
                    print(f"- {task.name} (Assigned to: {member.name})")



    def show_summary(self):
        total, done, pending = 0, 0, 0
        for member in self.members:
            for task in member.tasks:
                total += 1
                if task.status == "Completed":
                    done += 1
                else:
                    pending += 1
        print(f"\nTask Summary:")
        print(f"Total Tasks: {total}")
        print(f"Completed: {done}")
        print(f"Pending: {pending}")
