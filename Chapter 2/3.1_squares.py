def squares(n):
    slist = []
    for i in range(1, n):
        slist.append(i**2)
    return slist

sqs = squares(6)

# Duyệt list như thông thường.
for sq in sqs:
    print(sq)
