task=[]

def addTask():
    task = input("please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTask():
    if not tasks:
        print("There are no current tasks.")
    else:
        print("current tasks:")
        for index, task in enumerate(task):
            print(f"Task #{index}. {task}")
        
        



def deleteTask():
    listTasks()
    try:
      taskToDelete = int(input("enter the # to delete: "))
      if taskToDelete>=0 and taskToDelete < len(tasks):
          tasks.pop(taskToDelete)
          print(f"Task {taskToDelete} has been removed.")
      else:
          print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__== "__main__":
   print("welcome to the to-do list :)")
while True: 
    print("\n")
    print("Please select one of the following options")
    print("==============================================")
    print("1.Add a new task")
    print("2.Delete a task")
    print("3.List tasks")
    print("4.Quit")

    choice = input("Enter your choice: ")

    if(choice == "1"):
          addTak()

    elif(choice == "2"):
        deleteTask()

    elif(choice == "3"):
        listTask()

    elif(choice == "4"):
        break

    else:
        print("Invalid input. Please try again.")

  
        

      
