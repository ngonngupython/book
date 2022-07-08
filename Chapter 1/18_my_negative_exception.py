class MyNegativeException(BaseException):
  def __init__(self, value):
    super().__init__()
    self.value = value


# Sử dụng trong code.
number = -1


try:
  if number < 0:
    raise MyNegativeException("0 and positive number only")

  # Your other code here
except MyNegativeException:
  print("My customize Exception is throw")
except:
  print("Other Exception")
finally:
  print("This will execute no matter what")