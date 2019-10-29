import os
path = 'D://My_Python//Program//Python_Study//BUPT_homework//'
try:
    bmpf = open(path+'black.bmp', 'r+b')
    for i in range(128):
        if i in range(7, 17):
            bmpf.seek(118 + 64*i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\x99')
        elif i in range(27, 37):
            bmpf.seek(118 + 64 * i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\xaa')
        elif i in range(47, 57):
            bmpf.seek(118 + 64 * i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\xbb')
        elif i in range(67, 77):
            bmpf.seek(118 + 64 * i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\xcc')
        elif i in range(87, 97):
            bmpf.seek(118 + 64 * i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\xdd')
        elif i in range(107, 117):
            bmpf.seek(118 + 64 * i, os.SEEK_SET)
            for j in range(64):
                bmpf.write(b'\xee')
except IOError as e:
    print("error:", e)
    exit()
finally:
    bmpf.close()
