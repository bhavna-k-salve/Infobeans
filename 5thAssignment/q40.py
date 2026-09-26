


n = int(input("Enter a number:"))

odd = 0
even = 0

while n > 0:
  reminder = n % 10
  if reminder % 2 ==0:
    even += 1
  else:
    odd += 1  
  n //=10

  
print(f"Even is : {even}")
print(f"Odd is : {odd}")  