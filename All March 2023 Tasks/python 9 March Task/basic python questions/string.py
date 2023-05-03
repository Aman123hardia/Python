b=20
a="Hello {0}"
print(a.format(b))

c = "Hello, World!"
print(c[2:5])

d = "Hello, World!"
print(d.upper())


e= " Hello, World! "
print(e.strip())

f = "Hello, World!"
print(f.replace("H", "J"))


g = "Hello, World!"
h= g.split(",")
print(h)



txt = "Hello Sam!"
mytable = str.maketrans("l", "P")
print(txt.translate(mytable))


txt = "welcome to my world"
x = txt.title()
print(x)


txt = "   s   "
x = txt.isspace()
print(x) 