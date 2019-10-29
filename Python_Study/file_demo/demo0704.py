# demo0704.py
BasePath = 'D:\\My_Python\\Program\\Python_Study\\file_demo\\'
try:
    f1 = open(BasePath+'temp.txt', 'wb')
    # f1.write('123')                          # 错误：不能写入字符串，只能写入字节数据
    f1.write(b'123abc')
    a = bytearray(32)
    for ch in range(0, 32):
        a[ch] = 65				# 65为ASCII字符A
    f1.write(a)

    for ch in range(0, 32):
        a[ch] = ch				# ASCII字符0-31
    f1.write(a)
    # print(f1.read(3))          #不可从文件中读
except IOError as e:
    print("error:", e)
    exit()
finally:
    f1.close()
