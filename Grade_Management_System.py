import pandas as pd
data={}
a=True
print("Welcome to My GRADE MANAGEMENT SYSTEM")

while a:
    op=input('''What Operation would you like to perform:-
             1.Add Student(a)
             2.Update Student's info(u)
             3.Delete Student(d)
             4.View Student(v)
             5.Download(dd)
             6.Exit(e)
        ----->''')
    if op.lower()=='a':
        name=input("Enter the full name of the student: ")
        if name.isalpha()==False:
            print("Invalid Name")
            continue
        grade=int(input(f"Enter the grades of the student {name} out of 500: "))
        data[name]=grade
        print(f"Added student {name} with grades {grade}")
    elif op.lower()=='u':
        if len(data)==0:
            print("Data is empty")
            continue
        name=input("Enter the full name of the student to update: ")
        if name in data:
            new_grades=int(input(f"Enter the new grades of {name} out of 500: "))
            data[name]=new_grades
            print(f"Update grades of {name} with {new_grades}")
        else:
            print("Student Not Found")
            continue
    elif op.lower()=='d':
        if len(data)==0:
            print("Data is empty")
        name=input("Enter the full name of the student to delete: ")
        if name in data:
            del data[name]
            print("Deleted",name)
        else:
            print("Invalid Name")
    elif op.lower()=='v':
        if len(data)==0:
            print("Data is empty")
            continue
        df = pd.DataFrame(list(data.items()), columns=["Name", "Grade"])
        print(df)
    elif op.lower()=='dd':
        if len(data)==0:
            print("Data is empty")
            continue
        df = pd.DataFrame(list(data.items()), columns=["Name", "Grade"])
        csv=df.to_csv('Students_Data.csv')
    elif op.lower()=='e':
        print("Exiting...")
        break
    else:
        print('Operation Not Available')