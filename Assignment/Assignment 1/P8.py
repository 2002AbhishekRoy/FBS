days = int(input("Enter the Days : "))

years = days // 365
print(years, "Years")

r = days % 365
week = r // 7
print(week, "Weeks")

r2 = r % 7
print(r2, "Days")
