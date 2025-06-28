# logical operators
# 1. and
# 2. or
# 3. not

x = 2
y = 1
z = 5

print(x > y and z > y)
print(x < y and z > y)
print(x > y and y < z and z > x)
print(x > z or y < z)
print(not x > z)
print(not z < y and y > x)