



first = int(input("Enter a first number:"))
second = int(input("Enter a second number:"))

if first <= second:
  small = first
else:
  small = second
 
i = 1  
while i <= small:
  if first%i==0 and second%i==0:
    hcf = i
  i += 1

print(hcf)  
  
  