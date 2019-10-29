import numpy as np
from PIL import Image
# 读入数据arr，此处为手动设置
arr = np.array([[1,2,3,4,5],[1,1,1,1,1],[9,9,9,9,9],[0,0,0,0,0],[0,0,0,0,0]])
# 将元素类型更改为'uint8'
arr=np.array(arr, dtype='uint8')
arr=Image.fromarray(arr)
# 第一个参数为存储的地址和名称，第二个参数为存储的图片类型
arr.save('test.bmp', 'bmp')
