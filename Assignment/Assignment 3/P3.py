print("This Program input angles of a triangle and check whether triangle is valid or not.")

a1 = int(input("Enter the first angle : "))
a2 = int(input("Enter the second angle : "))
a3 = int(input("Enter the third angle : "))

if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 + a3) == 180:
    print("Valid Triangle")

else:
    print("Not a Valid Triangle")
