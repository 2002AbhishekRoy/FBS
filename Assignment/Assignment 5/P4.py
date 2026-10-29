print("This Program print Armstrong number within a given range.")

def armstrong(n):
    s = 0
    t = n
    
    while n > 0:
        d = n % 10
        s+=(d**3)
        n//=10

    if t == s:
        return True
    return False


a = int(input("From : "))
b = int(input("To : "))

for i in range(a,b+1):
    if armstrong(i):
        print(i)
