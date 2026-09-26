


import math

n = int(input("Enter a number: "))

print("Squares : ",end="")
for i in range(1,n+1):
  print(i**2,end=", ")
print()

print("Cube : ",end="")
for i in range(1,n+1):
  print(i**3,end=", ")  
print()  

print("Square root : ",end="")
for i in range(1,n+1):
  print(math.sqrt(i),end=", ")  
print()
  