#demo0706.py
import os
BasePath='c:\\data\\'
try:
    f1 = open(BasePath+'a21.txt','r+b')    #a21.txt必须存在，否则出错，读写方式打开
    #f1.write('123')                        #错误：只能写字节数据
    print(f1.read(3))                       #从文件中读取3个字符
    f1.write(b'789')
    f1.seek(0,os.SEEK_END)                  #定位到文件结束位置
    b = bytearray(10)                       #从文件中读取10个字节
    print(f1.readinto(b))                   #从文件中读取,因为指针已经在文件末尾，返回0
    f1.seek(0,os.SEEK_SET)                  #定位到文件开始位置
    print(f1.read())                        #读取文件的全部内容
    f1.seek(-15,os.SEEK_CUR)                #文件指针从当前位置（文件末尾）向前移动15个字节
    print(f1.readinto(b))                   #读出10个字节
    print(b)
except IOError as e:
    print(e)
    exit()
finally:
    f1.close()
