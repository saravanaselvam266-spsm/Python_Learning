class TodoList:
    #constructor
    def __init__(self):
        self.tasks = []
    
    #methods
    def add_task(self,id,task,status="pending"):
        current = {"id":id , "task":task ,"status":status}
        self.tasks.append(current)

    def view_tasks(self):
        print(self.tasks)

    def delete_task(self,task_id):
        self.task_id = task_id
        pass


variable = TodoList() # instance of a class
variable.add_task(id=1, task="Project Booking Page", status = "pending")
variable.view_tasks()

alex = TodoList()
alex.add_task(id=2,task="Conversation")
alex.view_tasks()