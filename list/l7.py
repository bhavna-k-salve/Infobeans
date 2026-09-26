

l = [5,4,3,10,21]

n = int(input("ENter a number:"))

for i in range(len(l)):
  if n == l[i]:
    print(f"yes {n} is in list and at {i}th index.")
    break
else:
  print(f"No {n} is not found in list ")  