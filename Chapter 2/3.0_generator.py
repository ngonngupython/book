# Tạo generator
myfirstgenerator = (x * x for x in range(10))
for mg in myfirstgenerator:
    print(mg, end=" ")


# không còn thông tin trong lần gọi thứ 2 với myfirstgenerator
for mg in myfirstgen:
    print(mg, end=" ")

