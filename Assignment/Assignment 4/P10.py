print("This Program check if given number is Perfect Number.")

n = int(input("Enter a number : "))

t = n

s = 0

for i in range(1, n):
    if n % i == 0:
        s+=i

if t == s:
    print("Perfect Number")
else:
    print("Not a Perfect Number.")
    
