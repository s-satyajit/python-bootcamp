x = "Satyajit"
y = 23
z = ["satyajit", "sports", 23]

a = "My name is {} & my age is {}".format(x, y)
b = "My name is {1} & my age is {0}".format(y, x)
c = f"My name is {x} & my age is {y}"
d = f"My name is {z[0]}, I love playing {z[1]} & my age is {z[2]}"

print(a)
print(b)
print(c)
print(d)