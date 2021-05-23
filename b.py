first_grade = float(input("Enter your first evaluation grade: "))
second_grade = float(input("Enter your second evaluation grade: "))
third_grade = float(input("Enter your third evaluation grade: "))
first_perc = second_perc = 0.30
third_perc = 0.40
first_weighted = first_grade*first_perc
second_weighted = second_grade*second_perc
third_weighted = third_grade*third_perc
final_grade = first_weighted+second_weighted+third_weighted
print("")
print("*"*10)
print(f"Final grade: {final_grade}")
