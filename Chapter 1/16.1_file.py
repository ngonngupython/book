# Ghi thông tin vào file

fname = "a_file.txt"
mode = "w"
afile = open(fname, mode)    

afile.write("Hello World.")  
afile.write("\n")                              # xuống dòng
afile.write("Hello World - 2.")
afile.write("\n")
afile.write("Hello World - 3.")
afile.close()


# Đọc dữ liệu từ file
fname = "a_file.txt"
mode = "r"
bfile = open(fname, mode)
print(bfile.read())
