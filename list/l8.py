

l = [5,4,6,2,4,9,8,7,4]

n = int(input("ENter a number: "))

result = []

for i in range(len(l)):
  if n == l[i]:
    result.append(i)
    
if result:
  print("the number is found at :",end=" ")    
  for i in result:
    print(i,end=" ")
else:
  print(f"number not found")  