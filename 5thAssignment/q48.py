


start = int(input("Enter a first number : "))
stop = int(input("Enter a last number : "))


for i in range(start,stop+1):
  print(f"Factors of {i} : ",end=" ")
  for j in range(1,i+1):
     if i%j==0:
         print(j,end=" ")
  print( )   
     




