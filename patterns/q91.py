

for i in range(1,6):
  if i<7:
    for k in range(1,7-i):
      print(" ",end="")
  if i<5:    
    for j in range(1,3):
      print(chr(64+i),end="")
    print()  
  else:
    for _ in range(1,10):
      print(chr(64+i),end="")
    print()  