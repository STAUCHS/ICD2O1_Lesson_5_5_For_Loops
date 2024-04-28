
num_of_students = int(input("Enter the number of students: "))
sum = 0

for i in range(num_of_students):
  mark = int(input("Enter a marK: "))
  sum = sum + mark

average = sum/num_of_students

print(f"The average for your class is: {average}")