print("This Program checks three digit Palindrome Number.")

def digit(n):
    c=0
    while n > 0:
        c+=1
        n//= 10

    return c

n = int(input("Enter the number : "))
r=0
t = n

if digit(n) == 3:
    while n > 0:
        d = n % 10
        r = (r * 10) + d
        n//= 10

    if t == r:
        print("Palindrome")

    else:
        print("Not Palindrome")

else :
    print("Not a 3 digit number")
