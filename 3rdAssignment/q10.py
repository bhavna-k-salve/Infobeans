

leap_year = int(input("Enter a year:"))

if leap_year%4==0 and leap_year%400==0 and leap_year%100 != 0:
  print("It is a leap year.")
else:
  print("It is not a leap year.")  