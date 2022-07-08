# *args
def string_concat2(*args):
    result = ""
    for arg in args:
        result += arg
    return result

# **kwargs
def afunc(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
