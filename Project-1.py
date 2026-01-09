print("Welcome to My Restaurant!")
print("Here is our menu:")
print("""        1.Dal Makhani ₹100
         2.Shahi Paneer ₹150
         3.Laccha Paratha ₹30
         4.Butter Roti ₹20""")
n=int(input("How many items do you want: "))
amount=0
for i in range(n):
    order=int(input("What would you like to order,Write the adjacent number of the item: "))
    if order==1:
        n1=int(input("In how much quantity do you want it: "))
        amount+=n1*100
    elif order==2:
        n2=int(input("In how much quantity do you want it: "))
        amount+=n2*150
    elif order==3:
        n3=int(input("In how much quantity do you want it: "))
        amount+=n3*30
    elif order==4:
        n4=int(input("In how much quantity do you want it: "))
        amount+=n4*20
    else:
        print("Item Not Available")
print(f"Your total payable amount is ₹{amount}")


