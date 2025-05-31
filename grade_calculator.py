grade = int(input('Grade: '))

# Calculate the grade letter equivalent
if grade >= 100:
    print("A")
elif grade > 90 and grade <= 99 :
    print("B")
elif grade > 80 and grade <= 89:
    print("C")
elif grade > 70 and grade <= 79:
    print("D")
elif grade > 60 and grade <= 69:
    print("D-")
else:
    print("F")
