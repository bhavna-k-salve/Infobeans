


for i in range(1,6):
  for j in range(1,i+1):
    if (i%2==0 and j%2==0) or (i%2==1 and j%2==1)  or i==j:
      print(1,end=" ")
    else:
      print(0,end=" ")  
  print()  