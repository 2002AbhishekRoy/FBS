print("This program Fibonacci series upto n.")

n = int(input("Enter the Limit : "))

a = 0
b = 1

print(a)
print(b)

for i in range(n-2):
    s = a + b
    print(s)
    a = b
    b = s
    
