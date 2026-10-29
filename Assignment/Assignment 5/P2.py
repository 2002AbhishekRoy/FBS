print("This Program Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.")

n = int(input("Enter no of students : "))

for i in range(n):
    print("For Student ", i+1)
    s1 = float(input("Enter the marks in Subject 1 : "))
    s2 = float(input("Enter the marks in Subject 2 : "))
    s3 = float(input("Enter the marks in Subject 3 : "))
    s4 = float(input("Enter the marks in Subject 4 : "))
    s5 = float(input("Enter the marks in Subject 5 : "))
    percentage = ((s1+ s2 + s3 + s4 + s5) / 500) * 100
    print("Result of Student ", i+1, "is : ", percentage)
    
