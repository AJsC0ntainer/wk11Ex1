
print("CALCULATOR APPLICATION")
score = float(input("What is a numeric score (0 - 100)?  "))
letterGrade = " "

if score >= 89.5 and score <= 100:
    letterGrade = "A"
elif score >= 79.5 and score < 89.5:
    letterGrade = "B"
elif score >= 69.5 and score < 79.5:
    letterGrade = "C"
elif score >= 59.5 and score < 69.5:
    letterGrade = "D"
else: 
    letterGrade ="F"
    
print(f"The letter grade for score {score} is: {letterGrade}")