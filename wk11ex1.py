#Program Title
print("CALCULATOR APPLICATION")
#Define, store score value from user input
score = float(input("What is a numeric score (0 - 100)?  "))
#Variable to strore the grade letter
letterGrade = " "
#Conditional for A grade
if score >= 89.5 and score <= 100:
    letterGrade = "A"
#Conditional for B grade
elif score >= 79.5 and score < 89.5:
    letterGrade = "B"
#Conditional for C grade
elif score >= 69.5 and score < 79.5:
    letterGrade = "C"
#Conditional for D grade
elif score >= 59.5 and score < 69.5:
    letterGrade = "D"
#Otherwise F Grade
else: 
    letterGrade ="F"
#Prints the score and the letter grade.
print(f"The letter grade for score {score} is: {letterGrade}")

#Pushed to GitHub Wk11Ex1 GitHub Repo.