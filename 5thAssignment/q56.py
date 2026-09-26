


start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))

factorial = 1
for number in range(start,stop+1):
  factorial *= number


print(f"Factorial is : {factorial}")  