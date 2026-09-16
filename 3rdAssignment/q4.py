

marks = int(input("Enter marks of student: "))


if marks >= 80:
  print("Grade 'A'")
elif marks >= 60 and marks < 80:
  print("Grade 'B'")   
elif marks >= 50 and marks < 60:
  print("Grade 'C'")  
elif marks >= 45 and marks < 50:
  print("Grade 'D'") 
elif marks >= 25 and marks < 45:
  print("Grade 'E'")     
elif marks < 25:
  print("Grade 'F'")   
else:
  print("Wrong input write correct number.")  