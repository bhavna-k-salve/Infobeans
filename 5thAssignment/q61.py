



start = int(input("Enter a first number : "))
stop = int(input("Enter a last number :"))



for leap_year in range(start,stop+1):
  if (leap_year%4==0 and leap_year%400==0) or leap_year%100!=0:
    print("It is a leap year.")
  else:
    print("It is not a leap year.")  

