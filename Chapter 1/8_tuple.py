# Khởi tạo
a_tuple = ()
print(type(a_tuple))

b_tuple = (1, 2, 3)

# Khởi tạo từ danh sách
c_tuple = tuple([1, 'two', 3.0, None, True])

# Khởi tạo từ chuỗi.
d_tuple = tuple('this is string')

# Một số thao tác khác
e_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(min(e_tuple), max(e_tuple), sum(e_tuple), len(e_tuple))

# Index và slicing
print(e_tuple[1] , e_tuple[4])
print(e_tuple[4:])
print(e_tuple[:4])