



for i in range(1,5):
  if i<5:
    for _ in range(1,5-i):
      print(" ",end="")
  for j in range(1,i*2):
    if i%2 != 1 and j%2==0 or (i==3 and (j==2 or j==4)):
      print("_",end="")
    else:  
      print("*",end="")
  print() 
  

for i in range(1,5): 
  for j in range(1,7):
    if i>=j or i+j>=8:
      print(" ",end="")
    elif i%2 == 0 and j%2==0  or (i==1 and (j==3 or j==5)):
      print("_",end="")  
    else:  
      print("*",end="")   
  print()   