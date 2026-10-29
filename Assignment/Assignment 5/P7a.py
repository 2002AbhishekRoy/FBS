print("Sereis : 1! + 2! + 3! + 4! + .....n!")

def fact(n):
    f = 1

    for i in range(1, n+1):
        f*=i

    return f

s = 0
n = int(input("Enter n : "))

for i in range(1, n+1):
    s+= fact(i)

print("Sum of sereis : ", s)
