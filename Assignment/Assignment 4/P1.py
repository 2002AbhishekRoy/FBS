print("This Program print all even numbers until n.")

n = int(input("Enter the limit : "))

print("The even numbers are : ")

for i in range(n):
    if i % 2 == 0:
        print(i)

