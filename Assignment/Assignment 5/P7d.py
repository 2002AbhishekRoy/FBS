print("a + a2 / 2 + a3 / 3 + ...... + a10 / 10")

a = int(input("Enter the value of a : "))
n = int(input("Enter the last limit : "))

s = 0

for i in range(1, n+1):
    s+= (a**i/i)

print("Sum of Sereis : ", s)
