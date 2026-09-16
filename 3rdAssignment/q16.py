
physics = int(input("Enter marks of physics: "))
chemistry = int(input("Enter marks of chemistry: "))
biology = int(input("Enter marks of biology: "))
mathe = int(input("Enter marks of mathe: "))
computer = int(input("Enter marks of computer: "))


percentage = (physics+chemistry+biology+mathe+computer)/5

if percentage >= 90:
  print("Grade 'A'")
elif percentage >= 80 and percentage < 90:
  print("Grade 'B'")   
elif percentage >= 70 and percentage < 80:
  print("Grade 'C'")  
elif percentage >= 60 and percentage < 70:
  print("Grade 'D'") 
elif percentage >= 40 and percentage < 60:
  print("Grade 'E'")     
elif percentage < 40:
  print("Grade 'F'")   
else:
  print("Wrong input write correct number.")  