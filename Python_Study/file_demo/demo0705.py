#demo0705.py
BasePath='c:\\data\\'
try:
    f1 = open(BasePath+'a21.txt','rb')         #a21.txt必须存在，否则出错
    #f1.write('123')                           #错误：只能读不能写
    print(f1.read(3))                          #从文件中读取3个字符
    b = bytearray(10)
    print("f1.readinto(b):",f1.readinto(b))    #从文件中读取10个字节
    print("b:",b)
    f1.seek(0)
    print("f1.read():",f1.read())              #读取文件的全部剩余内容
    print("f1.readinto(b):",f1.readinto(b))    #因为已经到文件尾，所以读出0个字节
except IOError as e:
    print(e)
    exit()
finally:
    f1.close()
