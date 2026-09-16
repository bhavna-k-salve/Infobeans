

math = int(input("enter a maths marks:"))
hindi = int(input("enter a hindi marks:"))
english = int(input("enter a english marks:"))
science = int(input("enter a science marks:"))
sanskrit = int(input("enter a sanskrit marks:"))


average = (math+hindi+english+science+sanskrit)/5

if average > 90:
  print("Merit")
elif average <= 90 and average >80:
  print("A")
elif average <= 80 and average > 70:
  print("B")
elif average <= 70 and average > 60:
  print("C")
elif average <= 60 and average > 50:
  print("D")
else:
  print("Fail")          