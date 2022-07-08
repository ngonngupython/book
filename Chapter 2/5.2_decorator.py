def mydivide(afunc):
  def inner(a, b):
    if b == 0:
      print("Can not divide by 0")
    else:
      return afunc(a, b)
  return inner


@mydivide
def libdivide(a, b):
  return a/b


#print(mydivide(1, 2))
#print(mydivide(1, 0))
print(libdivide(1, 0))