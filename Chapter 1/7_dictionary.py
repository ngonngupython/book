# Khai báo và hiển thị.
a_dictionary = { 'key' : 'value', 1: 'Bắc Ninh', 0: None} 
b_dictionary = {}
c_dictionary = dict()
d_dictionary = dict({1:2})

print(type(a_dictionary))
print(a_dictionary)
print(len(a_dictionary))

# Truy cập theo key
print(a_dictionary['key'], a_dictionary[1])
a_dictionary['key'] = 2
print(a_dictionary)

# Duyệt các phần tử
c_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
for k in c_dict:
    print(k, c_dict[k])
