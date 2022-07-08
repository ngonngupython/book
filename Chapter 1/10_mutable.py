a_list = [1, 2, 'three']

print(id(a_list))

a_list[1] = 'two'
print(id(a_list))