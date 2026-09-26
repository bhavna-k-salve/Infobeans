

n = int(input("Enter a number:"))
m = n
l = len(str(m))


sum = 0

for i in range(l):
  reminder = n%10
  sum += reminder  
  n = n//10
  
print(sum)  
  