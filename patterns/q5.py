

for i in range(9):
  for j in range(9):
    if (i <= 3 or i >= 5) and (j <= 3 or j >= 5):
      print(' ', end=" ")
    else:
      print(("*"), end=" ") 
  print()  