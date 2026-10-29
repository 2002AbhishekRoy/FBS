print("This program check if user has entered correct userid and password.")

user_id = "Abhishek@112"
password = "Python"

uid = input("Enter the User ID : ")
pwd = input("Enter the password : ")

if user_id == uid and password == pwd:
    print("Valid Credential")

    pin = 1234
    print(pin)
    user_pin = int(input("Enter the 4 digit number given above : "))

    if pin == user_pin:
        print("Successful")
    else:
        print("Unsuccessful")

else:
    print("Invalid Credential ")
