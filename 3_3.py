grade = float(input("Grade?:"))

if grade >1:
    print("Not a valid score")
    quit()
else:
    if grade >=0.9:
        letterGrade = "A"
    elif grade >=0.8:
        letterGrade = "B"
    elif grade >=0.7:
        letterGrade = "C"
    elif grade >=0.6:
        letterGrade = "D"
    elif grade <0.6:
        letterGrade = "F"

print(letterGrade)
