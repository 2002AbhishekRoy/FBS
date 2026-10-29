print("This program check if person is eligible to marry or not.")

name = input("Enter the name : ")
sex = input("Enter the sex (Male or Female) : ")
age = int(input("Enter the age : "))

if sex == "Male":
    if age >= 21:
        print("Eligible to Marry")

    else:
        print("Not Eligible to Marry")

if sex == "Female":
    if age >= 18:
        print("Eligible to Marry")

    else:
        print("Not Eligible to Marry")

        
    
