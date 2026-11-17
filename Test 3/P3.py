salary = int(input("Enter the basic salary : "))

if salary <= 20000:
    da = salary * (10/100)
    ta = salary * (12/100)
    hra = salary * (15/100)

    total_salary = salary + da + ta + hra
    print("Total Salary : ", total_salary)

else:
    da = salary * (15/100)
    ta = salary * (18/100)
    hra = salary * (20/100)

    total_salary = salary + da + ta + hra
    print("Total Salary : ", total_salary)
