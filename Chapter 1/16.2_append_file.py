mode = 'a'
cfile = open(fname, mode)
cfile.write("\n This is line 4th.")  
cfile.close()

bfile = open(fname, 'r')       # mở file trong phiên làm việc mới.
for line in bfile:             # có thể dùng for để duyệt từng dòng
    print(line)