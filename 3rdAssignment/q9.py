

char = input("Enter a character:")

if char >= 'a' and char <= 'z':
  print(f"{char} is a loiwercase")
elif char >= 'A' and char <= 'Z':
  print(f"{char} is a upparcase")
else:
  print("insufficient input.")    