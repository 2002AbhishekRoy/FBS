print("This Program print prime numbers between 1 to 100.")

def prime(n):
    if n <= 1:
        return False

    c = 0

    for i in range(2, (n//2)+1):
        if n % i == 0:
            c = 1
            break

    if c == 1:
        return False
    return True

n = int(input("Enter the limit :  "))

for i in range(n):
    if prime(i):
        print(i)
