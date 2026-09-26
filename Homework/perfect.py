

n = int(input("Enter a number:"))
sum = 0  
i = 1
while i <= (n//2)+1:
  if n % i == 0:
   sum += i
  i += 1


if n == sum:
  print("It is Perfect number.")    
else:
  print("It is not Perfect number")   