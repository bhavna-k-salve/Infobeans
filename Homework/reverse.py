

n = int(input("Enter a number to reverse:"))
m = n
l = len(str(m))

reverse = 0

for i in range(l):
  reminder = n%10
  reverse = reverse * 10 + reminder  
  n = n//10
  
print(reverse)  
  