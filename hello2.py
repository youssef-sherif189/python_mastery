msg ="i love python"
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


