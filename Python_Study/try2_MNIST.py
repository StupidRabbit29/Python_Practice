import struct
import numpy as np
import matplotlib.pyplot as plt

def load_MNIST(path,kind):#path和kind是str，kind是train或t10k；函数返回tuple
    with open(path+'/'+kind+'-labels.idx1-ubyte','rb') as flabel:#打开label文件
        magic_lb, n_lb = struct.unpack('>II',flabel.read(8)) #read()从文件中读取指定个数字节；unpack()将字节流转化为指定类型（int32),返回tuple
                                                    #文件最开始有两个4字节int分别是magic number（区分文件是图片还是标签）和number of items,
                                                    #'>'大端转小端；'II'指有两个int
        labels = np.fromfile(flabel , dtype=np.uint8) #按照uint8的格式从文件中读取数字，存入labels数组

    #print(magic,n,labels)

    with open(path+'/'+kind+'-images.idx3-ubyte','rb') as fimage:#打开image文件
        magic_im, n_im, row, col = struct.unpack('>IIII',fimage.read(16)) #read()从文件中读取指定个数字节；unpack()将字节流转化为指定类型（int32),返回tuple
                                                    #文件最开始有4个4字节int分别是magic number,number of image,number of rows（28）,number of columns（28）
                                                    #'>'大端转小端；'IIII'指有4个int
        images = np.fromfile(fimage , dtype=np.uint8) #按照uint8的格式从文件中读取数字，存入image数组
    return labels , images , n_lb

train_labels, train_images, train_num = load_MNIST('C://Users//付彬//Desktop//','train')
test_labels, test_images, test_num = load_MNIST('C://Users//付彬//Desktop//','t10k')
train_images=train_images.reshape(60000,784)
test_images=test_images.reshape(10000,784)
print(train_images,train_labels,test_images,test_labels)

##########统计数据
train_cnt=[0]*10
for i in range(train_num):
    train_cnt[train_labels[i]]=train_cnt[train_labels[i]]+1
print("训练集中0-9的标签的个数统计如下：",train_cnt)

test_cnt=[0]*10
for i in range(test_num):
    test_cnt[test_labels[i]]=test_cnt[test_labels[i]]+1
print("测试集中0-9的标签的个数统计如下：",test_cnt)


##########画图：显示前10个图像
fig, ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True, ) #将画布分成nrows * ncols个子图，每个图上呈现一个数字
ax = ax.flatten()#将ax由n*m的Axes组展平成1*nm的Axes组，之后可直接使用ax[i]
for i in range(10):#画出前10个图像
    img = train_images[i].reshape(28, 28) #将展开的一维向量reshape为28*28
    #ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[i].imshow(img, cmap='Greys') #灰色

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()

########显示同一个标签的数字
print("显示同一个标签的数字\n请输入要显示的数字（0-9）：")
number=int(input())
fig, ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True, ) #将画布分成nrows * ncols个子图，每个图上呈现一个数字
ax = ax.flatten()#将ax由n*m的Axes组展平成1*nm的Axes组，之后可直接使用ax[i]
cnt=0
i=0
while(cnt<10):#遍历训练集，找到label为number的样本并显示
    if train_labels[i]==number:
        ####显示数字
        img = train_images[i].reshape(28, 28) #将展开的一维向量reshape为28*28
        #ax[i].imshow(img, cmap='Greys', interpolation='nearest')
        ax[i].imshow(img, cmap='Greys')
        cnt=cnt+1
    i=i+1

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()