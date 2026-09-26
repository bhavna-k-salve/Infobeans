


start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))



for i in range(start,stop+1):
  reverse = 0
  m = i
  l = len(str(m))
  for j in range(l):
    reminder = i%10
    reverse = reverse * 10 + reminder  
    i = i//10
  print(reverse)  
  