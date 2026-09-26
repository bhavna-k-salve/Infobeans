

for i in range(1,5):
  k=1
  for j in range(4,0,-1):
    if i<j:
      print(" ",end=" ")
    else:
      print(k,end=" ")
      k+=1
  print()    
 
for i in range(1,4):
  k=1
  for j in range(1,5):
    if i>=j :
      print(" ",end=" ")
    else:
      print(k,end=" ")
      k+=1
  print()             