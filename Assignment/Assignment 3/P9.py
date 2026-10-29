print("This Program calculate the percentage of student based on marks of any 5 subjects.")
print("\nWe assume that each subject is of 100 marks.")
s1 = int(input("Enter the marks in Subject 1 : "))
s2 = int(input("Enter the marks in Subject 2 : "))
s3 = int(input("Enter the marks in Subject 3 : "))
s4 = int(input("Enter the marks in Subject 4 : "))
s5 = int(input("Enter the marks in Subject 5 : "))

percentage = ((s1+s2+s3+s4+s5)/500)*100;

print("You have scored : ",percentage,"%")

if percentage >= 90:
    print("First Class")

elif percentage >= 70 and percentage < 90:
    print("Second class")

elif percentage >= 50 and percentage < 70:
    print("Third Class")

elif percentage < 50:
    print("Fail")
