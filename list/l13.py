

l =[2,7,11,15]
target = 9
i = 0
j = len(l)-1

while i<j:
  sum = l[i]+l[j]
  if sum == target:
    result = [i,j]
    break
  elif sum> target:
    j-=1
  else:
    i += 1
    
print(result)      