print("This Program check if given number Strong Number.")

def fact(n):
    f = 1

    for i in range(1, n+1):
        f*=i

    return f


n = int(input("Enter a number : "))

t = n

s = 0

while n > 0:
    d = n % 10
    s+=fact(d)
    n //=10

if s == t:
    print("Armstrong Number")

else:
    print("Not a Armstrong number")
    
