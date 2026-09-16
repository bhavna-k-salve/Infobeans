
number = int(input("Enter a number:"))
reverse = 0
count = 0
if count < 4:
  reminder = number % 10
  reverse = reverse*10 + reminder
  number = number // 10
  count+= 1
  if count < 4:
    reminder = number % 10
    reverse = reverse*10 + reminder
    number = number // 10
    count+= 1
    if count < 4:
      reminder = number % 10
      reverse = reverse*10 + reminder
      number = number // 10
      count+= 1  
      if count < 4:
        reminder = number % 10
        reverse = reverse*10 + reminder
        number = number // 10
        count+= 1  
        
print(reverse)        