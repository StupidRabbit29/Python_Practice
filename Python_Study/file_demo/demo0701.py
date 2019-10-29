import os
try:
    # 打开当前目录下的文本文件dat.txt以便写入，file1为文件对象
    file1 = open(r"c:\code\dat.txt", "w")
    file1.write("10000")             #写入字符串10000
    for i in range(1000000):
        file1.write(str(i)+'\n')
        #file1.write(i)
except FileNotFoundError:         #文件读写操作可能发生异常，这里捕获三种异常，文件不存在，
                                  #没有足够操作权限和其它异常
    print("File not found error\n")
except PermissionError:
    print("Permission error\n")
except BaseException as e:
    print("Other unexpected error")
    print(e)
finally:
    #file1.close()
    print("File has been closed!")

