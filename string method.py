s="hello"
useful_methods= [m for m in dir(s) if "__" not in m]
print(useful_methods)
print(help(s.capitalize))
print(s.capitalize())
print("HELLO".casefold())
print("hello".center(30,"*"))
print("hello".center(30, " "))
print("I see a little dog".count("e"))
x= "i do not cook nor compare"
print(f"there are {x.count("o")} o's inside")
print("helloooollolololoolo".find("l", 10))
s5= "bob goes home to meet bob so the can take their bob amd go bobing"
pos=0
while True:
    start = s5.find("bob", pos)
    if start==-1:
        break
    print("found bob on position", start)
    pos= start+1
items= ["cat", "rat", "mouse", "house"]
print(", + another ".join(items))
print("i Like to go HIKIng!!".lower().upper())
print("i like to go hiking".title())
print("i like to go skiing".replace("skiing", "hiking"))
#lalala
