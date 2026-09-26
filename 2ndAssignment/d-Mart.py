
"\n\n"
print("-" * 50)
print("\t\t\t\t D-Mart")

customer_name = input("Enter Customer name:  ")
date = input("Enter a date: ")
gender = input("Enter customers gender: ")
if gender ==  "male":
  gift = "Cadeberry"
else:
  gift = "Ladger Wallet"
# item = 0

product1 = input("ENter a 1st product name :")
quantity1 = int(input(f"ENter quantity of your  {product1}:"))
price = 10
total_amount1 = price * quantity1
if quantity1 > 4:
  discount_percent = 5
  discount= (total_amount1 * 5)/100
else:
  discount = 0
after_discount1 = total_amount1 - discount    
  
product2 = input("ENter a 2nd product name :")
quantity2 = int(input(f"ENter quantity of your  {product2}:"))
price = 10
total_amount2 = price * quantity2
after_discount2 = total_amount2 - discount   

product3 = input("ENter a 3rd product name :")
quantity3 = int(input(f"ENter quantity of your  {product3}:"))
price = 10
total_amount3 = price * quantity3
after_discount3 = total_amount3 - discount  

product4 = input("ENter a 4th product name :")
quantity4 = int(input(f"ENter quantity of your  {product4}:"))
price = 10
total_amount4 = price * quantity4
after_discount4 = total_amount4 - discount  

product5 = input("ENter a 5th product name :")
quantity5 = int(input(f"ENter quantity of your  {product5}:"))
price = 10
total_amount5 = price * quantity5
after_discount5 = total_amount5 - discount  


product6 = input("ENter a 6th product name :")
quantity6 = int(input(f"ENter quantity of your  {product6}:"))
price = 10
total_amount6 = price * quantity6
after_discount6 = total_amount6 - discount  

product7= input("ENter a 7th product name :")
quantity7 = int(input(f"ENter quantity of your  {product7}:"))
price = 10
total_amount7 = price * quantity7
after_discount7 = total_amount7 - discount  

product8 = input("ENter a 8th product name :")
quantity8 = int(input(f"ENter quantity of your  {product8}:"))
price = 10
total_amount8 = price * quantity8
after_discount8 = total_amount8 - discount  

product9 = input("ENter a 9th product name :")
quantity9 = int(input(f"ENter quantity of your  {product9}:"))
price = 10
total_amount9 = price * quantity9
after_discount9 = total_amount9 - discount  

product10  = input("ENter a 10th product name :")
quantity10 = int(input(f"ENter quantity of your  {product10}:"))  
price = 10
total_amount10 = price * quantity10
after_discount10 = (total_amount10 * 15 )/100   
  
total_amount = total_amount1 + total_amount2 + total_amount3 + total_amount4 + total_amount5 + total_amount6 + total_amount7 + total_amount8 + total_amount9 + total_amount10

if total_amount <= 10000:
  after_discount = total_amount * 0.15
elif total_amount > 5000 and total_amount < 10000:
  after_discount = total_amount * 0.10
else:
  after_discount = 0  
  



carry_bag = input("do you like buy a carry bag(Yes/No):")
if carry_bag == 'Yes':
  bag = "yes"
else:  
  bag = "No"
  
price_bag = 10
gst = total_amount*0.10

total_amount = total_amount+gst
after_discount = after_discount + gst

print("\n\n")
print("-" * 50)
print("\t\t\t\t D-Mart")

print(f"Name :  {customer_name} \t\t Date : {date}")

print("-" * 50)

print("Iteam Name \t quantity \t price \t After-Discount")
print(f"{product1}\t {quantity1} \t{total_amount1} \t {after_discount1}")
print(f"{product1}\t {quantity1} \t{total_amount2} \t {after_discount2}")
print(f"{product1}\t {quantity1} \t{total_amount3} \t {after_discount3}")
print(f"{product1}\t {quantity1} \t{total_amount4} \t {after_discount4}")
print(f"{product1}\t {quantity1} \t{total_amount5} \t {after_discount5}")
print(f"{product1}\t {quantity1} \t{total_amount6} \t {after_discount6}")
print(f"{product1}\t {quantity1} \t{total_amount7} \t {after_discount7}")
print(f"{product1}\t {quantity1} \t{total_amount8} \t {after_discount8}")
print(f"{product1}\t {quantity1} \t{total_amount9} \t {after_discount9}")
print(f"{product1}\t {quantity1} \t{total_amount10} \t {after_discount10}")      
print("-" * 50)
print(f"\t\t\t\t { total_amount} \t {after_discount}")


print("-" * 50)

print("\t\t\t\t A.P\t D.P")

print(f"\t\t\t\t {total_amount}\t {after_discount}")
  
print(f"Gift  :-  {gift} \t\t0.00\t 0.00 ")



if bag == "yes":
  print("10:00\t 10:00")
  total_amount += 10
else:
  print("00:00\t 00:00")  
  total_amount += 0

  
  
gst = total_amount/10 + total_amount
print(f"GST (10%)\t\t\t{gst} \t {gst}")   
  
  
    
print("-"*50)  

print(f"\t\t\t\t{total_amount} \t {after_discount} ")
  
print("\t\tThankyou to\n\t\t visit\n\t\t D-Mart")  

print("-"*50)  