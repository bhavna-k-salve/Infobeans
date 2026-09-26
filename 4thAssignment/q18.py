
# 1  2  2  4  8  32



n = int((input("Enter a number: ")))

first = 1
second = 2
for i in range(1,n+1):
  print(first,end=", ")
  third =  first * second
  first = second
  second = third
  

