x = {'number': 1, 'name': 'blue', 'age': 200}

x['name'] = 'white'
print(x['number'])
print(len(x))
x['year'] = 2025
print(x.pop("age"))
print(x.popitem())
print(x)