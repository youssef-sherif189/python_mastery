# numbers 
# integer
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# float
print(type(0.1))
print(type(1.5))
print(type(10.5))
print(type(100.9))
print(type(-100.7))
print(type(0.99))

# complex
ComplexNumber = 5+6j
print(type(ComplexNumber))
print("real and imag parts is: {}".format(ComplexNumber))
print("real part is: {}".format(ComplexNumber.real))
print("imag part is: {}".format(ComplexNumber.imag))

# [1] you can convert from int to float or complex
# [2] you can convert from float to int or complex
# [3] you cannot convert from complex to any type 

print(100)
print(float(100))
print(complex(100))

print(99.98)
print(int(99.98))
print(complex(99.98))

print(10+9j)
# print(int(10+9j)) cannot convert

# addiction
print(10 + 30)
print(-10 + 20)
print(1 + 2.66)
print(1.2 + 1.2)

# Subtraction
print(60 - 30)
print(-30-20)
print(-30 - -20)
print(5.66 - 3.44)

# Multipliction
print(10 * 3)
print(5 + 10 * 100)
print((5 + 10) * 100)

# Division
print(100 / 20)
print(int(100 / 20))

# Modulus
print(8 % 2)
print(9 % 2)
print(20 % 5)
print(22 % 5)

#  Exponent (power)
print(2 ** 5)
print(2 * 2 * 2 * 2 * 2)
print(5 ** 4)

# Floor Division
print(100 // 20)
print(119 // 20)
print(120 // 20)
print(129 // 20)
print(140 // 20)


# Lists
# [1] List items are enclosed in square brackets
# [2] List are ordered, to use index to access item 
# [3] List are mutable => add, delete, edit 
# [4] List Items is not unique
# [5] List can have different data types
# -----------------------------------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]
print(myAwesomeList)
print(myAwesomeList[1])
print(myAwesomeList[-1])
print(myAwesomeList[-3])

print(myAwesomeList[1:4])
print(myAwesomeList[1:])
print(myAwesomeList[:4])

print(myAwesomeList[::1])
print(myAwesomeList[::2])

print(myAwesomeList)
myAwesomeList[1] = 2
print(myAwesomeList)
myAwesomeList[-1] = False
print(myAwesomeList)

myAwesomeList[0:3] = []
print(myAwesomeList)
myAwesomeList[0:3] = ["a", "b", "c"]
print(myAwesomeList)

# append()
myFriends = ["youssef", "sherif", "mohamed"]
myOldFriends = ["gods", "Loly", "Taha"]
myFriends.append("mo")
myFriends.append("100")
myFriends.append("150.99")
myFriends.append(True)
print(myFriends)
myFriends.append(myOldFriends)
print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()
a = [1, 2, 3, 4]
b = ["a", "b", "c"]
c = ["one", "two"]
a.extend(b)
a.extend(c)
print(a)

# remove 
x = [1, 2, 3, 4, "joe", True, "joe", "joe"]
x.remove("joe")
print(x)

# sort() ترتيب
y = [1, 2, 100, 120, -10, 17, 29]
y.sort()
print(y)
y.sort(reverse=True)
print(y)
J = ["A", "Y", "B", "Z"]
J.sort()
print(J)
J.sort(reverse=True)
print(J)

# reverse()
z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

#clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()
b = [1, 2, 3, 4, 5,]
c = b.copy()
print(b)
print(c)

b.append(5)
print(b)
print(c)

# count()
d = [1, 2, 3, 1, 3, 6, 10, 1, 9, 1,]
print(d.count(1))

#index
e = ["joe", "yasso", "godz", "ahmed", "ramy", "amr"]
print(e.index("ahmed"))

# insert()
f = [1, 2, 3, 4, 5, "a", "b"]
f.insert(0, "Test")
print(f)
f.insert(-1, "Test")
print(f)

# pop
g = [1, 2, 3, 4, 5, "a", "b"]
print(g.pop(0))
print(g.pop(3))
print(g.pop(4))
print(g.pop(-1))
