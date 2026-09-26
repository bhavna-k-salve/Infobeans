

start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))

for number in range(start,stop+1):
  i = 2
  count = 0
  while i < number:
    if number % i == 0:
      count += 1
    i += 1
    
  if count == 0:
    print(f"{number} is a prime number.") 
   