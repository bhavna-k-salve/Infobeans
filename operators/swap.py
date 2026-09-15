

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

print(f"Before a is : {a}")
print(f"Before b is : {b}")

a = a^b
b = a^b
a = a^b


print(f"After a is : {a}")
print(f"After b is : {b}")