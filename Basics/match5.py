

per = float(input("Enter a number:"))

match per:
  case per if per>90:print("A")
  case per if per>=80 and per<=90:print("B")
  case per if per>=60 and per<80:print("C")
  case _:print("D")