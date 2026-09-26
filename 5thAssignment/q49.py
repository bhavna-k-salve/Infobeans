



start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))

for i in range(start,stop+1):
  sum = 0  
  for j in range(1,(i//2+1)):
    if i % j == 0:
     sum += j
  if i == sum:
    print(f"{i}  is Perfect number.")    
  