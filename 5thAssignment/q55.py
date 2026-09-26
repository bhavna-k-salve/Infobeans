


start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))


for i in range(start,stop+1):
  if i%2!=0:
    print(i,end=", ")