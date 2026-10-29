print("This Program converts the time entered in hh,min and sec into seconds.")

hour = int(input("Enter the hour : "))
minute = int(input("Enter the minute : "))
second = int(input("Enter the seconds : "))

sec = (hour* (60 * 60)) + (minute*60) + second

print(sec, "seconds")
