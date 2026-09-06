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




