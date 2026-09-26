


n = int(input("Enter a number:"))
result = n
m = n
count = 0
while n > 0:
  count += 1
  n //=10

sum = 0  
for i in range(1,count+1):
  reminder = m % 10
  factorial = 1
  for i in range(1,reminder+1):
    factorial *= i
  sum += factorial
  m //= 10

if result == sum:
  print("It is Strong number.")    
else:
  print("It is not Strong number")   