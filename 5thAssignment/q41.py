

first = int(input("Enter a first number:"))
second = int(input("Enter a second number:"))

if first >= second:
  largest = first
else:
  largest = second
  
while True:
  if largest%first==0 and largest%second==0:
    break
  largest += 1
  
print(largest)  
  
  