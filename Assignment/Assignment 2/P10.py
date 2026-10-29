print("This Program reverses three-digit number.")

def digit(n):
    c=0
    while n > 0:
        c+=1
        n//=10
    return c


a = int(input("Enter the number : "))
r = 0
if digit(a) == 3:
    while a > 0:
        d = a % 10
        r =(r*10) + d
        a//=10

    print("Reversed Number : ",r)

else:
    print("Not a 3 digit number")
