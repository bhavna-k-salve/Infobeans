



start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))

for n in range(start,stop+1):
  m = n
  l = len(str(m))
  reverse = 0

  for i in range(l):
    reminder = n%10
    reverse = reverse * 10 + reminder  
    n = n//10
    
  
  if reverse == m:
    print(f"{reverse} It is a palindrome.")


















  