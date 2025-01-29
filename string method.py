s="hello"
useful_methods= [m for m in dir(s) if "__" not in m]
print(useful_methods)
print(help(s.capitalize))
print(s.capitalize())

