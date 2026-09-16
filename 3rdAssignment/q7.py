

numberHeld = int(input("How many days class is held:"))
classAttended = int(input("How many attendence:"))

percentage = (((365-numberHeld)-classAttended)*100)//365

if percentage >= 75:
  print("Student is allow to sit in exam.")
else:
  print("Student is not allow to sit in exam.")  