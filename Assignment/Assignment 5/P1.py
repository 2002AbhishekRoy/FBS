print("This Program prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.")

user_id = "Abhishekroy@12"
password = "Python"

uid = input("Enter the user id : ")
pwd = input("Enter the Password : ")


if uid != user_id or password != pwd:
    c = 0
    while c < 3:
        uid = input("Enter the user id : ")
        pwd = input("Enter the Password : ")

        c+=1


print("You are terminated.")
