
for i in range(1,7):
  if i<7:
    for k in range(1,7-i):
      print(" ",end=" ")
  for j in range(1,i*2):
    if j%2==0 and i%2==0:
      print("0",end=" ")
    else:
      print("1",end=" ")   
  print()     