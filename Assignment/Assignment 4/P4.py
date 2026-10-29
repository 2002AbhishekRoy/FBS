print("This Program print factorial of a number.")

n = int(input("Enter the number : "))

f = 1

for i in range(1, n+1):
    f*=i

print("Factorial of ", n, "is : ", f)
