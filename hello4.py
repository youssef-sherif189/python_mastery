#  Tupple
# tupple with one element
thestr1 = ("osama")
thestr2 = "osama"
print(thestr1)
print(thestr2)
print(type(thestr1))
print(type(thestr2))
mytuble1 = ("osama",)
mytuble2 = "osama",
print(mytuble1)
print(mytuble2)
print(type(mytuble1))
print(type(mytuble2))
print(len(mytuble1))
print(len(mytuble2))

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (9, 8, 7, 6)
c = a + b
d = a + ("J", "O", "E", True) + b
print(c)
print(d)

# Tuple, list, string repeat(*)

mystring = "Joe"
myList = [1, 2]
mytuple = ("A", "B")
print(mystring * 6)
print(myList * 6)
print(mytuple * 6)

# Methods => count()
a = (1, 2, 8, 4, 5, 8, 9)
print(a.count(8))

# Methods => index()
b = (7, 2, 9, 4, 5, 8)
print(b.index(2))
# print("the position of indetypesx is: " + b.index(2)) # Error
print("the position of index is: {:d}".format(b.index(2)))
print(f"the position of index is: {b.index(2)}")

# Tupple Destruct
a =("A", "B", 4, "C")
x, y, _, z = a # (or write) "A", "B", "C"
print(x)
print(y)
print(z)

# SET 
# [1] Set items are enclosed in curly braces 
# [2] Set items are not Ordered And Not Indexed
# [3] Set Indexing and Slicing cant be done 
# [4] Set has only Immutable data  () list and Dictare not
# [5] Set items is unique


Mysetone = {"joe", "sher", 100}
print(Mysetone)
# print(Mysetone[0])

# Slicing cant be done
Mysettwo = {1, 2, 3, 4,5, 6, 7}
print(Mysettwo)
# print(Mysettwo[0:3])

# Set has only Immutable data types
# Setthree = {"JOE", True, 100.5, 4,[5, 6, 1]} # unhashable type: 'list'
Setthree = {"JOE", True, 100.5, 4,(5, 6, 1)} 
print(Setthree)

# Set items is unique
SetFour = {1, 2, 3, 1, "joe", "one", "joe"}
print(SetFour)

 # Set Methods
# clear()
a = {1, 2, 3, 4}
a.clear()
print(a)

# union 
b = {"one", "two", "three"}
c = {"1", "2", "3"}
print(b | c)
print(b.union(c))

# add()
d = {4, 5, 6, 7}
# d.add(8, 9)
d.add(8)
d.add(9)
print(d)

# copy()
e = {1, 2, 3, 4}
f = e.copy()
print(e)
print(f)

e.add(6)
print(e)
print(f)

# remove()
g = {1, 2, 3, 4, 5, 6}
g.remove(1)
# g.remove(7)
print(g)

# discard()
u = {2, 4, 6, 8, 9}
u.discard(2)
u.discard(7)
print(u)

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()
j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)
print(j)
print("=" * 40)
# Set Methods
# part 2

# diffirence()
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, "joe", 'sherif'}
print(a)
print(a.difference(b)) # a - b
print(a)

print("=" * 40)

# diffirince_update()
c = {1, 2, 3, 4, 5}
d = {1, 2, 3, "joe", 'sherif'}
print(c)
c.difference_update(d) # c - d
print(c)

print("=" * 40)

# intersection()
e = {1, 2, 3, 4, "X", "Joe"}
f = {"Joe", "X", 2}
print(e)
print(e.intersection(f)) # e & f
print(e)
print("=" * 40)

# intersection_update()
g = {1, 2, 3, 4, "X", "Joe"}
h = {"Joe", "X", 2}
print(g)
g.intersection_update(h) # e & f
print(g)
print("=" * 40)

# symmetric difference()
k = {1, 2, 3, 4, 5, "X"}
l = {"Joe", "X", 1, 2, 4, "Y"}
print(k)
print(k.symmetric_difference(l)) # k ^ l
print(k)
print("=" * 40)

# symmetric difference update()
i = {1, 2, 3, 4, 5, "X"}
j = {"Joe", "X", 1, 2, 4, "Y"}
print(i)
print(i.symmetric_difference_update(j)) # i ^ j
print(i)
