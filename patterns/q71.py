


for i in range(1,6):
  char = 65
  for j in range(1,i+1):
    if ((j==1 or i==j) and i<5) or i==5:
      print(chr(char),end="")
    else:  
      print(" ",end="")
    char += 1    
  print()  