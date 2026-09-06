a = "I Love Python"
print(a.index("P")) # This will print the index of the first occurrence of the character "P" in the string "I Love Python", which is 7
print(a.index("P", 0, 10)) # This will print the index of the first occurrence of the character "P" in the string "I Love Python" between index 0 and 10, which is 7
 # print(a.index("P", 0, 5)) # This will raise a ValueError because the character "P" is not found in the string "I Love Python" between index 0 and 5

b = "I Love Python"
print(b.find("P")) # This will print the index of the first occurrence of the character "P" in the string "I Love Python", which is 7
print(b.find("P", 0, 10)) # This will print the index of the first occurrence of the character "P" in the string "I Love Python" between index 0 and 10, which is 7
print(b.find("P", 0, 5)) # This will print -1 because the character "P" is not found in the string "I Love Python" between index 0 and 5

c = "youssef"
print(c.rjust(20))
print(c.rjust(20, "#"))
print(c.ljust(20, "#"))


e = """first line
second line
third line"""
print(e.splitlines()) # This will print a list of the lines in the string e, which is ['first', 'second', 'third']

d = "first line\nsecond line\nthird line"
print(d.splitlines()) # This will print a list of the lines in the string d, which is ['first line', 'second line', 'third line']

f  = "hello\tworld\tI\tlove\tpython"
print(f)
print(f.expandtabs(2)) # This will print the string f with tab characters expanded to 2 spaces
print(f.expandtabs(20))

one = "I Love Python And I 3G"
two = "I Love Python And I 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = "i love python"
six = "I Love Python"
print(five.islower())
print(six.islower())

seven = "youssef_3mk"
eight = "Youssef3mk100"
nine = "Youssef--3mk"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaBbbbbb"
y = "AaaaaaBbbbbb111112222"
print(x.isalpha())
print(y.isalpha())

d = "AaaaaaBbbbbb"
z= "AaaaaaBbbbbb111112222"
print(d.isalnum())
print(z.isalnum())

l = "Hello One Two Three One One"
print(l.replace("One", "1")) # This will replace all occurrences of the substring "One" with "1" in the string l, resulting in "Hello 1 Two Three 1 1"
print(l.replace("One", "1", 1)) # This will replace the first two occurrences of the substring "One" with "1" in the string l, resulting in "Hello 1 Two Three One"
print(l.replace("One", "1", 2)) # This will replace the first two occurrences of the substring "One" with "1" in the string l, resulting in "Hello 1 Two Three 1 One"

myList = ["Youssef", "sherif", "3mk"]
print(" ".join(myList)) # This will join the elements of the list myList into a single string, separated by spaces, resulting in "Youssef sherif 3mk"
print("-".join(myList)) # This will join the elements of the list myList into a single string, separated by hyphens, resulting in "Youssef-sherif-3mk"
print(", ".join(myList))
print(type(", ".join(myList)))

name = "Youssef"
age = 18 
rank = 100
print("myname is : " + name)
print("myname is: %s "% name)
print("myname is: %s and my age is : %d" % (name, age))
print("myname is : %s and my age is : %d and my rank is : %f " % (name , age , rank))

# %s => string
# %d => integer or number
# %f => float

n = "Youssef"
l = "AI"
y = 10

print("Iam %s and I work in %s and I have %d years of experience" % (n,l,y))

x = "Yassin"
z = "bmw company"
y = 9
print("I am %s and work in %s and I have %d years of experience" % (x,z,y))

myNumber = 10
print("my Number is: %d" % myNumber)
print("my Number is: %f" % myNumber)
print("my Number is: %.2f" % myNumber)

# myLongString = "Hello Every One I Am Youssef"
# print("Massage is %s" % myLongString)
# print("Massage is %.5s" % myLongString)

myLongString = "Youssef Love All Muslim And Want Anyone To Be Best"
print("Massage is %s" % myLongString)

