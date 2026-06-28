salary = int(input("Salary: "))

late_days = int(input("Late days: "))

absent_days = int(input("absent_Days: "))

if late_days>5:
    salary = salary - (salary*5)

if late_days>10:
    salary = salary - (salary*10)