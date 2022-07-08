def sum(a, b):
    return a + b


print(sum(1, 2))

lplus = lambda a, b: a + b
print(lplus(1,2))

print( (lambda a, b: a+b)(1, 2) )