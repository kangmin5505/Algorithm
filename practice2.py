a = [1,2,3]
b = a
c = [1,2,3]
print(id(a), id(b), id(c))
print(a is b)
print(a is c)