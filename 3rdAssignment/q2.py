

quantity = int(input("how many quantity did you purchased ?:"))
if quantity > 1000:
  discount = quantity // 10
  amount = (quantity*100) - discount
  print(f"Your have to pay {amount}")
else:
  print(f"you have to pay: {quantity*100}")  