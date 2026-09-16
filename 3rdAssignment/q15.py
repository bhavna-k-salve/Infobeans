

cost = int(input("ENter a cost price:"))

if cost > 100000:
  print("Tax is 15%")
elif cost >50000 and cost <= 100000:
  print("Tax is 10%")
elif cost <= 5000:
  print("Tax is 5%")
else:
  print("Insufficint input.")       