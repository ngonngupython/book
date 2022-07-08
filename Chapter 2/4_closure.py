def a_function():
    a_variable = "Xin Chào"
    def b_function(a_name):
        print(a_variable, a_name)

    return b_function

c = a_function()
c("Bình")
print(c.__closure__[0].cell_contents)
print(c)