#demo0710.py
BasePath='c:\\data\\'
import os
fd = os.open(BasePath+'os.dat',os.O_RDWR|os.O_CREAT)
print(fd)
os.write(fd,b'123')         #写入'123'
os.lseek(fd,-3,os.SEEK_CUR)  #从当前位置往回3个字符的位置
print(os.read(fd,2))         #输出的内容为b'12'
os.write(fd, b'abcdef')     #从第三个字符的位置开始写入新的内容
os.lseek(fd,0,os.SEEK_SET)  #定位到文件开始位置
print(os.read(fd,100))      #输出前100个字符的内容
