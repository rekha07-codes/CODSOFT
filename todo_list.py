print("=== MY TO-DO LIST ===")

task_list = []

while True:

    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    option = input("\nEnter your option: ")

    if option == "1":
        new_task = input("Enter your task: ")
        task_list.append(new_task)
        print("Task added successfully!")

    elif option == "2":
        if len(task_list) == 0:
            print("No tasks found.")
        else:
            print("\nYour To-Do List: ")
            count = 1
            for item in task_list:
                print(count, ".", item)
                count += 1

    elif option == "3":
        if len(task_list) == 0:
            print("No tasks available to remove.")
        else:
            print("\nYour To-Do List: ")
            count = 1
            for item in task_list:
                print(count, ".", item)
                count += 1

            remove = int(input("Enter the task number to remove: "))

            if remove >= 1 and remove <= len(task_list):
                    removed_task = task_list.pop(remove - 1)
                    print(removed_task, "has been removed.")
            else:
                    print("Invalid task number.")

    elif option == "4":
        print("Thank you for using the To-Do List.")
        break

    else:
        print("Invalid option!") 
