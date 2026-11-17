print("1/1! + 2/2! + 3/3! + 4/4! + ... N/N!")

def fact(n):
    f = 1
    i = 1
    
    while i <= n:
        f*=i
        i+=1

    return f

n = int(input("Enter the max limit : "))

s = 0

for i in range(1, n+1):
    s+=(i/fact(i))

print(s)
