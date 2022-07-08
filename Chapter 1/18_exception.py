try:
    #1 + "2"         # (1) 
    #1 / 0           # (2)
    raise            # (3)
except TypeError:
    print("Lỗi thao tác khác kiểu dữ liệu")
except ZeroDivisionError:
    print("Lỗi chia cho 0.")
except Exception as ex:
    print("Lỗi xảy ra là:", ex)
