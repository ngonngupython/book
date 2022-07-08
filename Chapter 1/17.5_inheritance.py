class Person:
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = addres

class Student(Person):     # khai báo kế thừa
  def __init__(self, name, age, address, student_no):
    super().__init__(name, age, address)    # gọi hàm khởi tạo lớp Person
    self.student_no = student_no                  # thuộc tính riêng của lớp Student

class Lecturer (Person):   # khai báo kế thừa
  def __init__(self, name, age, address, employee_no):
    super().__init__(name, age, address)      # gọi hàm khởi tạo lớp Person
    self. employee_no = employee_no           #thuộc tính riêng của lớp Lecturer
