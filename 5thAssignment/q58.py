

number = int(input("Enter a number:"))

binary = 0
place = 1

while number > 0:
  rem = number % 2
  binary = binary + rem * place
  number = number//2
  place = place * 10
  
print(binary)