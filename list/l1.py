import sys

# x = [10,20,30,40,50]

# print(x)
# x.append(100)
# print(x)

# x[0] = 90
# print(x)

# y = [12,"hello",True]
# print(y)
# print(y[0])
# print(y[1])
# print(y[2])

# print(id(y))

# for i in y:
#   print(i)


# for i in range(len(x)):
#   print(i)
#   print(x[i])
  
# print(type(x))  
# print(len(x))


z=[]


# print(type(z))


print(sys.getsizeof(z))

z.append(1)
print(sys.getsizeof(z))
z.append(2)
print(sys.getsizeof(z))
z.append(3)
print(sys.getsizeof(z))
z.append("hello")
print(sys.getsizeof(z))
z.append(5)
print(sys.getsizeof(z))




# a=10
# print(sys.getsizeof(a))


