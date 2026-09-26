

l = [5,4,3,10,21]


sum_even = 0
sum_odd = 0

for i in l:
  if i%2==0:
    sum_even += i
  else:
    sum_odd += i  
    
print(f"sum_even ={sum_even}")
print(f"odd_sum = {sum_odd}")