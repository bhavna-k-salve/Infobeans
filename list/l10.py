


l1 = [2,3,3,4,5]
l2 = [1,3,4,4,6,7,8]

i= 0
j = 0
result = []

while i <len(l1) and j < len(l2):
  if l1[i] < l2[j]:
    result.append(l1[i])
    i+=1
  else:
    result.append(l2[j])  
    j+=1

if i < len(l1):
  result.append(l1[i])
  i+=1

if j <len(l2):
  result.append(l2[j])    
  j+=1
  
  
print(result)    