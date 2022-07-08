# break
for i in range(7):
    print(i, end =" ")
    if 4 < i:
        break

# continue
for i in range(10):
    if i < 4:
        continue
    print(i, end=" ")
    
# break và continue
b_var = 10
while True:
    b_var -= 1
    if 5 < b_var:
        continue
    print(b_var, end=" ")
    if b_var < 0:
        break
