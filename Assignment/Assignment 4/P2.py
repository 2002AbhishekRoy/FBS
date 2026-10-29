print("This Program print all odd numbers until n.")

n = int(input("Enter the limit : "))

print("The odd numbers are : ")

for i in range(n):
    if i % 2 != 0:
        print(i)

