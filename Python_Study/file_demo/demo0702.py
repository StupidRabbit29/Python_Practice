#demo0702.py
BasePath='c:\\data\\'
try:
    f1 = open(BasePath+'a1.txt', 'w')      #若a1.txt存在，则清空其内容再写入。如果不存在，则创建。只写模式。
    f2 = open(BasePath+'b1.txt', 'r+')    #b1.txt必须存在。r+可支持写入
    f3 = open(BasePath+'c1.txt', 'w+')    #c1如果不存在，则自动创建。如果存在，则覆盖。读写模式。
    f4 = open(BasePath+'d1.txt', 'a+')    #添加模式，在文件末尾添加数据
    f1.write('123')                 #清空原有内容，重新写入新的数据
    #f1.write(123)                  #错误，只能写入字符串
    f2.write('123')                 #只覆盖当前位置（起始位置）的3个字符的内容，但不影响后面的内容
    print("b1:",f2.read())          #读出的是b1.txt的第4个字符到文件末尾的全部内容
    f3.write('123')                 #在当前文件位置（起始位置）写入新数据
    print("c1:",f3.read())          #读出内容为空
    f4.write('abc')                 #在文件末尾添加新的内容
    print("d1:",f4.read())          #读出内容为空
except IOError as e:
    print(e)
    exit()
finally:
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    print("closed!!!")