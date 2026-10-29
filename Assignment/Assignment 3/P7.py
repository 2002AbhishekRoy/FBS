print("This program check if user has entered correct userid and password.")

user_id = "Abhishek@112"
password = "Python"

uid = input("Enter the User ID : ")
pwd = input("Enter the password : ")

if user_id == uid and password == pwd:
    print("Valid Credential")

else:
    print("Invalid Credential ")
