name = input("Enter employee name: ")
name = name.strip()
name = name.title()
hour_worked = int(input("Enter hours worked: "))
hourly_wage = float(input("Enter hourly wage: "))
print(f"{name} earned {hourly_wage*hour_worked} this weak.")