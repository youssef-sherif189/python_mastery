# homworkes


# print("\n" +"=" * 30)
# print("  USER PROFILE REPORT  ")
# print("=" * 30)
# print(f"Name: {hello}")
# print(f"Email: {email}")
# print(f"Age: {age}")
# print("=" * 30)

# hello = input("enter your name; ")
# age = input("enetr your age; ")
# contry = input("enter your contry; ")

# print(f"name: {hello}")
# print(f"age: {age}")
# print(f"contry: {contry}")


# hello = input("enter your name: ")
# age =input("enter your age: ")
# contry = input("enter your contry; ")

# print(f"hello: {hello}", f"i am: {age} years old", f"i live in: {contry}")

name = "youssef"
print(type(name))
age = "18"
print(type(age))
x = "chaniese"
print(type(x))

# name =input('enter your name : ') 
# age =input('enter your age: ')
# c =input('enter your country')

# print(f"hello {name} how are you doing ,your age is {age} ,and my country is {c}")

# name =input('enter your name : ') 
# age =input('enter your age: ')
# c =input('enter your country')
# print(f"""hello {name} how are you doing
# your age is {age}
# my country is {c}""")

x = 1+2j
print("real part : {}".format (x.real))
print("complex part : {}".format (x.imag))

num = 10
print(f"{num:.10f}")
print("{:.10f}".format(num))

num = 159.650
print(int(num))

print(100 - 115) 
print(50 * 30) 
print(21 % 4)
print(110 / 11)
print(97 // 20)

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends [0])
print(friends [-5])
print(friends [-1])
print(friends [4])

print(friends [0::2])
print(friends [1::2])

print(friends [1:4])
print(friends [3:5])
friends[3:] = ["elzero", "elone"]
print(friends[:5])

friends = ["joe", "yasso", "sasa"]
friends.insert(0, "Nasser")
print(friends)
friends.append("salem")
print(friends)

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
print(friends[2:])
print(friends[2:4])

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

name ='youssef'
print(name[1])
print(name[2])
print(name[-1])
name ="youssef"
print(name[1:3])
print(name[4:6])
name ="#@#@youssef#@#@"
print(name.strip("#, @"))
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))
name_one = "youssef"
print(name_one.rjust(20, "@"))
name_two = "youssef_sherif"
print(name_two.rjust(20, "@"))

name_three = "YoUSsEf"
name_four = "yOusSeF"
print(name_three.swapcase())
print(name_four.swapcase())

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

name = "Elzero"
print(name.rfind("z"))
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "love", 1))
print(msg.replace("<3", "love"))
name = "Osama"
age = 38
country = "Egypt"
print(f"my name Is {name} my age is {age} my country is {country}") 
# print(f"my name Is {name}", f"my age is {age}", f"my country is {country}")
# week ( 4 )

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
print({*nums, *letters})

nums.update(letters)
print(nums)
nums.add("A")
nums.add("B")
nums.add("C")
print(nums)
nums.intersection(letters)
print(nums)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
my_set.discard("C")
print(my_set)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}
print(a.issubset(b))


hm = {
"HTML" : "90%",
"CSS" : "80%",
"PYTHON" : "30%"
}
# print(hm)
hm.update({"AI" : "20%"})
print(f'"HTML Progress is {hm["HTML"]}"')
print(f'"CSS PROGRESS IS {hm["CSS"]}"')
print(f'"PYTHON PROGRESS IS {hm["PYTHON"]}"')
hm.update({"AI" : "20%"})
print(f'"AI PROGRESS IS {hm["AI"]}"')




