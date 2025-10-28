from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n===== 🗂️ TASK MANAGER MENU =====")
        print("1 )  Add Member")
        print("2 )  Assign Task")
        print("3 )  Complete Task")
        print("4 )  View Tasks")
        print("5 )  View Members")
        print("6 )  Overdue Tasks")
        print("7 )  Summary Report")
        print("8 )  Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            name = input("Enter member name: ")
            age = int(input("Enter member age: "))
            manager.add_member(name, age)

        elif choice == "2":
            member_name = input("Enter member name: ")
            task_name = input("Enter task name: ")
            difficulty = input("Enter difficulty (Easy/Medium/Hard): ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            manager.assign_task_to_member(task_name, member_name, difficulty, deadline)

        elif choice == "3":
            member_name = input("Enter member name: ")
            task_name = input("Enter task name: ")
            manager.complete_task(member_name, task_name)

        elif choice == "4":
            member_name = input("Enter member name to view tasks: ")
            manager.show_member_tasks(member_name)

        elif choice == "5":
            manager.show_all_members()

        elif choice == "6":
            manager.show_overdue_tasks()

        elif choice == "7":
            manager.show_summary()

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
