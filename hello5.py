# Set Methods
# part 3
# issuperset
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b)) # True
print(a.issuperset(c)) # False
print("=" * 20)
# issubset()
d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}
print(d.issubset(e))
print(d.issubset(f))
print("=" * 20)
# isdisjoint()
g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {11, 12, 33, 44, 55}
print(g.isdisjoint(h))
print(g.isdisjoint(i))

#-------------------------
#-- Dictionary
# [1] Dict items are enclosed in curly braces  
# [2] Dict items are contains key : value
# [3] Dict key need to be immutable => (numbers, string, tuple) list not allowed
# [4] Dict value can have any date type 
# [5] Dict key needs to be unique 
# [6] Dcit is not ordered you access its element with key
# ----------- 

# Dictionary 
user = {
"name" : "joe",
"age" : "18",
"country" : "egypt",
(1, 2, 3, 4) : "test",#(1, 2, 3, 4):"test" (unhashable type: 'list')
"skills": ["Html", "Css", "Js"],
"rating": 10.5
}
print(user)
print(user['country'])
print(user.get("skills"))
print(user.keys())
print(user.values())

# Two Dimensional Dictionary
languages = {
"one" : {
"name" : "Js",
"progress" : "70%"
},
"two" : {
"name" : "Python",
"progress" : "80%"
},
"three" : {
"name" : "Css",
"progress" : "90%"
}
}
print(languages)
print(languages["one"])
print(languages["two"]["name"])
# Dictionary Length
print(len(languages))
print(len(languages["two"]))

# Create Dictionary from variables

frameworkone = {
"name": "Vuejs",
"progress": "80%"
}

frameworktwo = {
"name": "reactjs",
"progress": "90%"
}
frameworkthree = {
"name": "angular",
"progress": "80%"
}

allframework = {
"one": frameworkone,
"two": frameworktwo,
"three": frameworkthree
}
print(allframework)
# --------------------------------------
# Didctionary Methods
# Clear
user = {"name" : "Joe"
}
print(user)
user.clear()
print(user)

# Update
member = {"name" : "Joe"
}
member["age"] = 18
print(member)
member.update({"country" : "egypt"})
print(member)
# Copy
main = {"name" : "Joe"
}
print(main)
b = main.copy()
print(b)
main.update({"skills" : "Hakking"})
print(main)
print(b)
# keys & values 
print(main.keys())
print(main.values())
print("=" * 40)
# setdefault()
user = {
"name": "Joe"
}
print(user) 
# print(user.setdefault("name", "yassin"))
print(user.setdefault("age", 18))
print(user)
print("=" * 40)
# popitem()
member = {
"name" : "Joe",
"age" : 18
}
print(member)
member.update({"contry" : "egypt"})
print(member.popitem())
print("=" * 40)
# items()
view = {
"name" : "Joe",
"Skills" : "Ps"
}
allitems = view.items()
print(view)
view["age"] = 18
print(view)
print(allitems)
print("=" * 40)
#  fromkeys()
a = ("mykeyone", "mykeytwo", "mykeythree")
b = "J", "O", "E"
print(dict.fromkeys(a, b))
print("=" * 40)
# ----------------------
#    -- Boolean -- 
# ---------------------------
# [1] In Programing You Need To known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True
# ------------------------------
name = (" ")
print(name.isspace())
print("=" * 40) # =======
print(100 > 200)
print(100 > 100)
print(100 > 100.5)
print(100 > 90)
print("=" * 40)# ==========
# True Values
print(bool("Joe"))
print(bool({1, 2, 3}))
print(bool('JOE'))
print(bool(99))
print(bool(100.99))
print(100 > 90)
print(bool([1, 2, 3, 4]))
print(bool(True))
print("=" * 40)# ===============
# False Values
print(bool(0))
print(100 > 100)
print(100 > 100.5)
print(bool(""))
print(bool())
print(bool({}))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool(None))
print(bool(False))
 
