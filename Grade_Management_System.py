data={}
a=True
print("Welcome to My GRADE MANAGEMENT SYSTEM")

while a:
    op=input('''What Operation would you like to perform:-
             1.Add Student(a)
             2.Update Student(u)
             3.Delete Student(d)
             4.View Student(v)
             5.Exit(e)''')
    if op.lower()=='a':
        name=input