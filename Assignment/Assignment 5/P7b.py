print("N + N^2 + N^3+N^4 .....+N^N")

a = int(input("Enter the a : "))
n = int(input("Enter the last limit : "))

s = 0

for i in range(1, n+1):
    s+=(a**i)

print("Sum of sereis : ", s)
