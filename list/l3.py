# import sys

# l1 = [10,20,30]
# print(len(l1))
# # print(sys.getsizeof(l1))

# #Adding 

# l1.append(100)

# print("After")
# print(len(l1))
# print(sys.getsizeof(l1))


# l1.append(200)

# print("After")
# print(len(l1))
# print(sys.getsizeof(l1))






# insertion

# l1 = [10,20,30]
# print(len(l1))
# l1.insert(2,58)

# print(l1)

# l1.insert(50,800)
# print(l1)

# l1.insert(-40,80)
# print(l1)


#append and extend

# l2 = [10,20,30,40]

# print(l2)

# l2.append([1000,2000])

# print(l2)



#extend


# l2.extend([100,200])
# print(l2)


# l1 =[10,20,30]
# l2 = [40,50,60]
# l1.append(l2)
# print(l1)
# l1.extend(l2)
# print(l1)



#updation

# l = [10,20,30,40,50,60,70,80,90,100]

# l[1]=200

# l[2:6]=['a','b','c','d','e']
# print(l)

# l1 = [10,20,30]

# l1[:] = [1,2,3,4]
# print(l1)



#remove

l = [10,20,30,40]
print(l)
l.remove(40)
print(l)
l.pop(2)
print(l)




#clear and del

#clear      # return empty error
l.clear()
print(l)

#del(l)    # name error
print(l)