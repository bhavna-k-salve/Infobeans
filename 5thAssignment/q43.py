


binary_number = int(input("Enter a binary number:"))

decimal = 0 
power = 0

while binary_number > 0:
  digit = binary_number % 10
  decimal = decimal + digit * (2 ** power)
  binary_number //= 10
  power += 1
  
print(decimal)  