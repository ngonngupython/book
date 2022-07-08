# Khai báo lớp
class Person:
   def __init__(self, name, age):              # hàm khởi tạo constructor
     self.name = name
     self.age = age
   def info(self):
     print("Bạn", self.name, self.age, "tuổi.")

# Tạo object p từ class Person
p = Person("An", 8)
print(p.info())                                    # sử dụng phương thức
print(p.name)                                      # truy cập vào thuộc tính
