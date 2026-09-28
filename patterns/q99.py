


for i in range(1,5):
  if i<5:
    for _ in range(1,5-i):
      print(" ",end="")
  for j in range(1,i*2):
    print("*",end="")
  print() 
  

for i in range(1,5): 
  for j in range(1,7):
    if i>=j or i+j>=8:
      print(" ",end="")
    else:  
      print("*",end="")   
  print()   