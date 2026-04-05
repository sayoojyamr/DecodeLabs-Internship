my_tasks =[]

while True:
    print("\n...TO-DO-LIST...")
    print("1. Add task")
    print("2. Display task")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter a task: ")
        my_tasks.append(task)
        print("Task added...")
        
    elif choice == "2":
        print("\n Your Tasks:")
        for i,t in enumerate(my_tasks,1):
            print(i,t)
              
    elif choice == "3":
        print("Exit..")
        break
    
    else:
        print("Invalid input..")
        
        
    
        
