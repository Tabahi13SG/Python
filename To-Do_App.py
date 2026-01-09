a=True
tasks=[]
j=1

print("||Radhe Radhe||                                              ||Jai Shri Shyam||")
print("                          Welcome To My TO-DO APP")

while a:
    inp=input("What function do you want to perform a[add task] u[update any task] d[delete task] v[view tasks] e[exit]: ")
    if inp.lower()=='a':
        task=input("Enter the task you want to add: ")
        tasks.append(task)
        print(f"Added task to tasks list.")

    elif inp.lower()=='u':
        n=int(input("Enter the index of task you want to update: "))
        if n>len(tasks):
            print("Invalid Index")
            continue
        task_updated=input("Enter the task to update: ")
        tasks[n]=task_updated
        print("The updated task",n)

    elif inp.lower()=='d':
        n=int(input("Enter the index of task to delete: "))
        if n>len(tasks):
            print("Invalid Index")
            continue
        del tasks[n]
        print("Deleted task",n)

    elif inp.lower()=='v':
        for i in tasks:
            print(f"{j}. {i}")
            j+=1

    elif inp.lower()=='e':
        a=False
        print("Exiting...")

    else:
        print("Function not available")
    j=1