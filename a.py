name = input("Enter your name: ")
worked_hours = float(input("How many hours did you work?: "))
price_x_hour = float(input("Enter your price per hour (S./): "))
discount_perc = 0.15;
gross_salary = worked_hours*price_x_hour
discount = gross_salary*discount_perc
salary=gross_salary-discount
print("")
print("*"*10)
print(f"Worker : {name}")
print(f"Gross Salary : S./{gross_salary}")
print(f"Discount (15%): S./{discount}")
print(f"Salary : S./{salary}")
print("*"*10)
