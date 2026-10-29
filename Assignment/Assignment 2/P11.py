n = int(input("Enter a number : "))

fh = n // 500
n = n % 500

th = n // 200
n = n % 200

h = n // 100
n = n % 100

f = n // 50
n = n % 50

t = n // 20
n = n % 20

ten = n // 10
n = n % 10

five = n // 5
n = n % 5

two = n // 2
n = n % 2

one = n // 1
n = n % 1

total = fh + th + h + f + t + ten + two + one

print(total)
