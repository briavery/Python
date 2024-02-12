grade = int(input("Enter the numeric grade:"))

if grade > 100 or grade <0:
    print("The grade is outside the range>")

elif 90 <= grade <= 100:
    print("The letter grade is: A")

elif 80 <= grade <= 89:
    print("The letter grade is: B")

elif 70 <= grade <= 79:
    print("The letter grade is: C")

elif 60 <= grade <= 69:
    print("The letter grade is: D")

else:
    print("The letter grade is: F")