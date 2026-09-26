



start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))


for i in range(start,stop+1):
  print(f"Table of {i} : ",end=" ")
  for j in range(1,11):
     print(f"{i*j}",end=" ")
  print( )   
     
  