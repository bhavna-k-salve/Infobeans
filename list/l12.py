

n = [1,5,6,8,7,9]

target = 12
result = []
flag = False
for i in range(len(n)-1):
  for j in range(i+1,len(n)):
    if n[i] + n[j] ==target:
      result.extend([i,j])
      print(result)
      
      # exit()
      