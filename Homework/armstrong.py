
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
  sum += (reminder ** count)
  m //= 10

if result == sum:
  print("It is armstrong number.")    
else:
  print("It is not armstrong number")   