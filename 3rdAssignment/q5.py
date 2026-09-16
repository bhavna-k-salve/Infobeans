

person1 = int(input("Enter the age of 1st person:"))
person2 = int(input("Enter the age of 2nd person:"))
person3 = int(input("Enter the age of 3rd person:"))

if person1 > person2 and person1 >person3:
  print("1st person is a oldest and its age is: ",person1)
elif person2 > person3:
  print("2nd person is a oldest person and its age is: ",person2)
else:
  print("3nd person is a oldest person and its age is: ",person3)  
if person1 < person2 and person1 < person3:
  print("1st person is a youngest and its age is: ",person1)
elif person2 < person3:
  print("2nd person is a youngest person and its age is: ",person2)
else:
  print("3nd person is a youngest person and its age is: ",person3) 
      