def squares2(n):
    for i in range(n):
        yield i**2                 # trả về bình phương của i, 

sqs2 = squares2(6) 
for sq in sqs2:             # cú pháp duyệt không thay đổi.
    print(sq)
