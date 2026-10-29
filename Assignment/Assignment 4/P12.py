print("This Program check if given number is Armstrong number or not.")

n = int(input("Enter a number : "))

t = n

s = 0

while n > 0:
    d = n % 10
    s+= (d**3)
    n //= 10

if s == t:
    print("Armstrong Number")

else:
    print("Not a Armstrong Number")
