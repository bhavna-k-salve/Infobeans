


print("1.Addition")
print("2.Sustraction")
print("3.multiplication")
print("4.break")


choice = input("Enter a choice:")

a = int(input("ENter a number:"))
b = int(input("Enter second number:"))
while True:
  match choice:
    case "1":print(a+b)
    case "2":print(a-b)
    case "3":print(a*b)
    case "4": break
    case _:print("Invalid input...")