'''
Sử dụng is, is not khi so sánh giá trị Singleton thay vì dùng dấu ==.
'''

# Nên
if person is None:
    pass

# Không nên
if person == None:
    pass


'''
Sử dụng is not thay vì not is
'''

# Nên
if person is None:
    pass

# Không nên
if not person is None:
    pass


'''
Không nên sử dụng == khi so sánh các giá trị kiểu Boolean
'''

# Nên
if valid:
    pass

# Không nên
if valid == True:
    pass

if valid == False:
    pass

if valid is True:
    pass

'''
Kiểm tra một chuỗi bắt đầu hay kết thúc bởi chuỗi khác, 
sử dụng startswith hoặc endswith thay vì cắt chuỗi slicing và so sánh giá trị.
'''

# Nên
if file_name.startswith("ABC_"):
    pass
if file_name.endswith("pkl"):
    pass

# Không nên
if file_name[:4] == "ABC_":
    pass

if file_name[-3:] == "pkl":
    pass