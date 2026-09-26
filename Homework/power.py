

x = int(input("Enter a number of x :"))
y = int(input("ENter a number of y :"))

sum = 1
for _ in range(1,y+1):
  sum *= x
  
print(sum)  