

number = int(input("Enter a number : "))

i = 2
count = 0
while i < number:
  if number % i == 0:
    count += 1
  i += 1
  
if count == 0:
  print(f"{number} is a prime number.") 
else:
  print(f"{number} is not a prime number.")     