

number = int(input("Enter a number: "))

first = 0
second = 1
i = 0
if number <= 0:
  print("Please enter a positive number.")
else:
  while i<=number:
    print(first,end=" ")
    third = first + second
    first = second
    second = third
    i+=1