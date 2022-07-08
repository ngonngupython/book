# String
a_string = 'This is a string'
print(a_string)

x_string = """
This is string
in
multiple lines
"""

print(a_string[0], a_string[1], a_string[10], a_string[-1], a_string[-2])

# Slicing string
print(slicing_string[2:4])
print(slicing_string[4:])
print(slicing_string[2:-2])

# Others
print(len('0123456789'))
print('1' in '0123456789')

loop_string = "0123456789"
for ls in loop_string:
    print(ls, end=" ")