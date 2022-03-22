try :
    gradeScore = float(input("Grade Score?"))
except :
    print("Invalid grade score")
    quit()
def autoGrade(x) :
    float(x)
    if x >= 0.9 :
        grade = "A" 
    elif x >= 0.8 :
        grade = "B"
    elif x >= 0.7 :
        grade = "C"
    elif x >= 0.6 : 
        grade = "D"
    elif x < 0.6 :
        grade = "F"
    return grade
if gradeScore <= 1.0 :
    letterGrade = autoGrade(gradeScore)
else :
    print("Invalid grade score: must be less than or equal to 1.0")
    quit()
print("The grade is:" , letterGrade)
