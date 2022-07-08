import re

str = "Tổng số tiền 123456 VNĐ. Trong đó 123000 chi phí cho X, 456 cho Y."
pattern = "[0-9]+"

match = re.search(pattern, str)
print(match.group())

math2 = re.findall(pattern, str)
print(math2)