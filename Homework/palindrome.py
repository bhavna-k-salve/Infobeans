


n = int(input("Enter a number:"))
m = n
l = len(str(m))

reverse = 0

for i in range(l):
  reminder = n%10
  reverse = reverse * 10 + reminder  
  n = n//10
  
 
if reverse == m:
  print("It is a palindrome.")
else:
  print("It is not palindrome.")  
   
  