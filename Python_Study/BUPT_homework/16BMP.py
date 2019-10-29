import os
path = 'D://My_Python//Program//Python_Study//BUPT_homework//'
try:
    bmpf = open(path+'black.bmp', 'r+b')
    bmpf.seek(118, os.SEEK_SET)
    # temp = bytearray(1024)
    # print(bmpf.readinto(temp))
    # print(temp)
    # print(bmpf.read())
    for i in range(128):
        for j in range(64):
            bmpf.write(b'\x00')
        #if i in range(59, 69):          # 白色十字的横线部分
        #    bmpf.seek(118 + 64*i, os.SEEK_SET)
        #    for j in range(64):
        #        bmpf.write(b'\xff')
        #else:           # 白色十字的每一行的竖线部分
        #    bmpf.seek(118 + 64*i + 29, os.SEEK_SET)
        #    bmpf.write(b'\x0f\xff\xff\xff\xff\xf0')
except IOError as e:
    print("error:", e)
    exit()
finally:
    bmpf.close()
