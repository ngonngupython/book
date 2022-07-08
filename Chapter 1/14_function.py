def a_function():
    pass
    
    
def b_function():
    print("Xin chào")
    
    
def c_function(amount, price):
    sum = amount * price
    print("Số tiền phải thanh toán là", sum)
        
        
c_function(4, 20.5)


def d_function(amount, price):
    sum = amount * price
    return sum


sum = d_function(4, 20.5)
