print("This Program calculates total salary of employee based on basic.")

salary = int(input("Enter the salary : "))

da = salary * (10/100)

ta = salary * (12/100)

hra = salary * (15/100)

total_salary = salary + da + ta + hra

print("Total Salary : ", total_salary)
