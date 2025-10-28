# importing all the libraries
from member import Member
from task import Task
from utils.file_handler import save_data,load_data




class Task_Manager:
    
    # initialize the constructior with a list of members
    def __init__(self):
        self.MemberList = []


    #add members
    def add_memnber(self,member):
        self.MemberList.append(member)

    #assign task to members 
    def assign_task(self,member_name , task):
        pass

    # showing all task
    def show_all_task(self):
        for member in self.MemberList:
            print(f"{member.name}'s tasks :")
            for task in member.tasks :
                print(f"- {task}")



    def show_pending_task(self):
        for member in self.MemberList:
            for task in member.tasks :
                if task.status=='pending':
                    #if task is pending then showing the task and the member name 
                    print(f"- {task} - assigned to {member.name}")


    def show_overdue_tasks(self):
        for member in self.MemberList:
            for task in member.Tasks:
                #showing all the task which are delayed
                if task.isOverDue():
                    print(f"{task.name} -> assigned to : {member.name} ")

    
    def show_summury(self):
        # total tasks 
        # how many was done 
        # and how many is pending
        total , done , pending = 0  ,  0  ,  9
        for member in self.MemberList:
            for task in member.tasks :
                total+=1
                if task.status=='Completed':
                    done+=1
                else:
                    pending+=1
        print(f"total     : {total}")
        print(f"completed : {done}")
        print(f"pending   : {pending}")



    
    def show_leaderboard(self):
        pass


    def serach_task(self):
        pass



    def save(self):
        #member is a list which will store member's data as a dictionary
        data = {"members":[]}

        for member in self.MemberList:
            #converting member data into dictionary
            member_data = {
                "name":member.name,
                "age":member.age,
                "points":member.points,
                "tasks":[task.to_dict() for task in member.tasks] #we are storing list of tasks(dictionary)
            }
            data['members'].append(member_data)                   #addpening the member's data into the main data
        save_data("data/tasks.json",data)                         #saving to the tasks.json file



    def load(self):
        data = load_data('data/tasks.json')
        