#demo0703.py
BasePath='c:\\data\\'
try:
    f1 = open(BasePath+'a11.txt', 'r')      #a11.txt必须存在，否则出错
    f2 = open(BasePath+'b11.txt', 'r+')    #b11.txt必须存在。r+可读可写。
    #f1.write('123')   #错误：只能读不能写
    print("f1.read(3):", f1.read(3))       #从文件中读取3个字符
    print("f1.readline():", f1.readline()) #从文件中读取一行内容
    print("f1.read():", f1.read()) #读取文件的全部剩余内容
    f2.write('123')               #覆盖当前位置3个字符的内容，但不影响后面的内容
    print("f2.read():", f2.read()) #读出的是b11.txt的第4个字符到文件末尾的全部内容
except IOError as e:
    print(e)
    exit()
finally:
    f1.close()
    f2.close()

