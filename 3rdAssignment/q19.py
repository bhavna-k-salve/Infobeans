

number1 = int(input("Enter a first number:"))
number2 = int(input("Enter a second number:"))

choice = input("Enter your choice('+'','>'','=='' ) : ")

if choice == "+":
  print(f"Addition of both number is: {number1+number2}.")
elif choice == ">":
  if number1 > number2:
    print(f"Greatest number is: {number1}.")
  else:
    print(f"Greatest number is: {number2}.")    
elif choice == "==":
  if number1 == number2:
    print("Both number are equal.")
  else:
    print("Both number are not equal.")      
else:
  print("Invalide input.")    