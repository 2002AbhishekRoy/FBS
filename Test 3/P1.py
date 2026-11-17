print("This program print first n prime numbers.")

def prime(n):
    if n <= 1:
        return False

    i = 2

    while i <= n//2:
        if n % i == 0:
            return False

        i+=1

    else:
        return True

n = int(input("Enter the max limit : "))

for i in range(1, n+1):
    if prime(i):
        print(i)
