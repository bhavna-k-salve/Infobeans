


age = int(input("Enter your age:"))
gender = input("Enter your gender (M or F): ")
maritalStatus = input("Are you married or not(Y or N)? :")

if gender == 'F':
  print("She will work in urban areas.")
elif gender == 'M': 
  if(age>=20 or age<=40):
    print("he may work in anywhere")  
  elif (age>=40 or age<=60):
    print("he will work in urban areas only.")
else:
  print("ERROR")    