def mydivide(afunc):
  # Sử dụng closure
  def inner(a, b):
    if b == 0:
      print("Can not divide by 0")
    else:
      return afunc(a, b)
  return inner


def libdivide(a, b):
  return a/b


afunc = mydivide(libdivide)
print(afunc(1, 2))
print(afunc(1, 0))