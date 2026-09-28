


n = int(input("Enter a number:"))

last = n% 10
count = 0
temp = n
while temp:
  count += 1
  temp = temp//10
  
first =  n//(10 ** (count-1))
middle = n%(10 ** (count-1))
middle //= 10


n = n//10
n = n % (10**(len(str(n))-1)) 

result = first * (10 ** (count-1))+middle * 10 + last


print(result)