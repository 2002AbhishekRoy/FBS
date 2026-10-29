print("This program finds the sum of three-digit number.")

def digit(n):
    c=0
    while n > 0:
        c+=1
        n//=10
    return c

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if digit(a) == 3 and digit(b) == 3:
    s = a + b
    print("Sum : ", s)

else:
    print("Not a 3 digit number")
