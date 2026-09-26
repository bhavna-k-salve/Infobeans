


for i in range(6,0,-1):
  for j in range(1,7):
    if j>i:
      if j-2==i or j-4==i:
        print(0,end=" ")
      else:  
        print(1, end=" ")
    else:
      print(" ", end=" ")  
  print()  