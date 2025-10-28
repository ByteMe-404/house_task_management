class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tasks = []
        self.points = 0



    def assign_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.name}' assigned to {self.name}.")



    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                if task.status == "Completed":
                    print("Task already completed.")
                    return
                task.mark_complete()
                if task.difficulty.lower() == "easy":
                    self.points += 5
                elif task.difficulty.lower() == "medium":
                    self.points += 10
                elif task.difficulty.lower() == "hard":
                    self.points += 15
                print(f"Task '{task.name}' marked as completed! Total points: {self.points}")
                return
        print(f"Task '{task_name}' not found for {self.name}.")



    def show_tasks(self):
        if not self.tasks:
            print(f"{self.name} has no tasks assigned.")
            return
        print(f"\nTasks for {self.name}:")
        for task in self.tasks:
            print(f" - {task}")



    def __str__(self):
        return f"{self.name} (Age: {self.age}) — {len(self.tasks)} tasks, {self.points} pts"
