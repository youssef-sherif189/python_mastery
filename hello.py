# When The Fille Create
# Write 
print(type(10)) # This will print the type of the integer 10, which is <class 'int'>

print(type(-100)) # This will print the type of the integer -100, which is <class 'int'>

print(type(100.9)) # This will print the type of the float 100.9, which is <class 'float'>

print(type(1.9876545)) # This will print the type of the float 1.9876545, which is <class 'float'>

print(type("hello python")) # This will print the type of the string "hello python", which is <class 'str'>

print(type(['1','2','3','4','5','6','7'])) # This will print the type of the list ['1','2','3','4','5','6','7'], which is <class 'list'>

print(type((1,2,3,4,5,6,7))) # This will print the type of the tuple (1,2,3,4,5,6,7), which is <class 'tuple'>

print(type({'name':'hello','age':20,'city':'new york'})) # This will print the type of the dictionary {'name':'hello','age':20,'city':'new york'}, which is <class 'dict'>

print(type({'one':1,'two':2,'three':3,'four':4,'five':5})) # This will print the type of the dictionary {'one':1,'two':2,'three':3,'four':4,'five':5}, which is <class 'dict'>

print(type(2 == 2)) # This will print the type of the boolean value True, which is <class 'bool'>

My100Variable = "my Value" # This will print the value of the variable My100Variable, which is "my Value"

print(My100Variable) # This will print the value of the variable My100Variable, which is "my Value"

Name = "MY VALUE" # This will print the value of the variable Name, which is "MY VALUE"

print(Name) # This will print the value of the variable Name, which is "MY VALUE"

name = "Joe" # This will print the value of the variable name, which is "Joe"
myName = "Joe" # This will print the value of the variable myName, which is "Joe"
my_name = "Joe" # This will print the value of the variable my_name, which is "Joe"
print(name) # This will print the value of the variable name, which is "Joe"
print(myName) # This will print the value of the variable myName, which is "Joe"
print(my_name) # This will print the value of the variable my_name, which is "Joe"

X = 10 # This will print the value of the variable X, which is 10
print(X) # This will print the value of the variable X, which is 10
X = "Hello" # This will print the value of the variable X, which is "Hello"
print(X) # This will print the value of the variable X, which is "Hello"

hello = "yassin" # This will print the value of the variable hello, which is "yassin"
print(hello) # This will print the value of the variable hello, which is "yassin"

a, b, c = 1, 2, 3 # This will print the values of the variables a, b, and c, which are 1, 2, and 3 respectively
print(a) # This will print the value of the variable a, which is 1
print(b) # This will print the value of the variable b, which is 2
print(c) # This will print the value of the variable c, which is 3

print("Hello\bworld") # This will print "Hello" and then overwrite the "o" with a backspace
print("hello \
i love \
python") # This will print "hello ", then a newline, then "i love ", another newline, and finally "python"

print("i love backslash \\") # This will print "i love backslash \" with a single backslash

print('l love single quote \'test\'') # This will print "l love single quote 'test'" with single quotes around the word test

print("l love double quote \"test\"") # This will print "l love double quote "test"" with double quotes around the word test

print("hello word\nsecond line") # This will print "hello word" on the first line and "second line" on the second line (LINE FEED)

print("123456\rabcde") # This will print "abcde" on the same line as "123456" (CARRIAGE RETURN)

print("hello\tworld") # This will print "hello" followed by a tab space and then "world" 

print("\x41") # This will print the character represented by the hexadecimal value 41, which is "A"

msg = "i love python"
lang = "veryy much"

print(msg+lang)
print(msg+" "+lang)

a = "frist \
secound \
third"
b = "1 \
2 \
3"
print(a + " "+ b)

mystringone = 'this single quote string' # This is a single quote string
mystringtwo = "this double quote string" # This is a double quote string
print(mystringone)
print(mystringtwo)
mystringthree = 'this single quote "test"' # This is a single quote string with a double quote inside
mystringfour = "this double quote 'test'" # This is a double quote string with a single quote inside
print(mystringthree)
print(mystringfour)
mysrtingfive = '''first
secound
third
four''' # This is a triple quote string with multiple lines
mysrtingsix = """1
2
3
4""" # This is a triple quote string with multiple lines
print(mysrtingfive)
print(mysrtingsix)

myString = "I Love Python" 
print(myString[0]) # This will print the first character of the string "I Love Python", which is "I"
print(myString[2])
print(myString[-1]) # first character form end This will print the last character of the string "I Love Python", which is "n"
print(myString[0:5]) # This will print the first five characters of the string "I Love Python", which is "I Lov"
print(myString[:10]) # This will print the first ten characters of the string "I Love Python", which is "I Love Pyt"
print(myString[10:]) # This will print the characters of the string "I Love Python" starting from index 10 to the end, which is "on"

print(myString[:]) #full data
print(myString[::1]) #full data with step of 1
print(myString[::2]) #full data with step of 2
print(myString[::3]) #full data with step of 3

a = "   I Love Python   "
print(a.strip()) # This will print the string "I Love Python" without the leading and trailing spaces
print(a.rstrip()) # This will print the string "   I Love Python" without the trailing spaces
print(a.lstrip()) # This will print the string "I Love Python   " without the leading spaces

b = "###I LOVE PYTHON###"
print(b.strip("#")) # This will print the string "I LOVE  PYTHON" without the leading and trailing "#" characters
print(b.rstrip("#")) # This will print the string "### I LOVE  PYTHON" without the trailing "#" characters
print(b.lstrip("#")) # This will print the string "I LOVE  PYTHON ###" without the leading "#" characters
c = "@#@#@#I LOVE PYTHON@#@#@"
print(c.strip("@#"))
print(c.rstrip("@#"))
print(c.lstrip("@#"))

b = "I Love 2d Graph and 3g Tec and python"
print(b.title())

b = "I love 2d Graph and 3g Tec and python"
print(b.capitalize())

c, d, e, y = "1" , "11" , "111" , "1111"
print(c)
print(d)
print(e)
print(y)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(y.zfill(3))

g= "Youssef"
print(g.upper())

h = "YoUssef"
print(h.lower())

a = "I Love Python and PHP MYSQL"
print(a.split())

b= "I-Love-Python-and-PHP-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-MySQL"
print(c.split("-" , 2))

d = "I-Love-Python-and-PHP-MySQL"
print(d.rsplit("-" , 2))

# center
e = "youssef"
print(e.center(7))
print(e.center(9, "#"))
print(e.center(17, "@"))

# count()
f = "I Love Python and PHP bec PHP is easy"
print(f.count("PHP"))
print(f.count("PHP", 0, 25)) # only one PHP word is in the first 25 characters of the string

# swapcase()
g = "I Love Python"
h = "i lOVe pYTHON"
print(g.swapcase())
print(h.swapcase())

# startswith()
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S")) # false bec not start with s
print(i.startswith("P", 7, 12))

# endswith()
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("P")) # false bec not end with P
print(j.endswith("e", 2, 6))