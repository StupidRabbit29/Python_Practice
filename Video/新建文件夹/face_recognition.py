# -*- coding: UTF-8 -*-

import sys, os, dlib, glob, numpy, cv2
from skimage import io

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# 1.人脸关键点检测器
predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
# 3.候选人脸文件夹
faces_folder_path = "initial_images/"
# 4.需识别的人脸
img_path = "frame/200.jpg"

# 1.加载正脸检测器
detector = dlib.get_frontal_face_detector()
# 2.加载人脸关键点检测器
sp = dlib.shape_predictor(predictor_path)
# 3. 加载人脸识别模型
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

# win = dlib.image_window()
# 候选人脸描述子list
descriptors = []


# 对文件夹下的每一个人脸进行:
# 1.人脸检测
# 2.关键点检测
# 3.描述子提取

def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)
    save_path = r'frame/'
    count = 0
    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

        if (count % 20 == 0):
            cv2.imwrite(save_path + str(count) + '.jpg', frame)
        count = count + 1
        print(count)
        # 显示图像并等待10毫秒按键输入，输入‘q’退出程序
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = io.imread(f)
    # win.clear_overlay()
    # win.set_image(img)

    # 1.人脸检测
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        # 2.关键点检测
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        # 转换为numpy array
        v = numpy.array(face_descriptor)
        descriptors.append(v)

# 对需识别人脸进行同样处理
# 提取描述子，不再注释


# cv2.namedWindow("Test_video")
save_path = r'frame/'
count = 0
# 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ok, frame = cap.read()  # 读取一帧数据
    if not ok:
        break

    if (count % 20 == 0):
        cv2.imwrite(save_path + str(count) + '.jpg', frame)

        img = io.imread(save_path + str(count) + '.jpg')
        dets = detector(img, 1)
        dist = []
        ii = 0
        x = []
        y = []
        #print("here")
        for k, d in enumerate(dets):
            shape = sp(img, d)
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            d_test = numpy.array(face_descriptor)
            x.append(int((d.right() + d.left()) / 2))
            y.append(d.bottom())

            cv2.rectangle(img, (d.left(), d.bottom()), (d.right(), d.top()), (0, 255, 0), 4)
            cv2.imwrite(save_path + str(count) + '.jpg', img)
            # 计算欧式距离
            for i in descriptors:
                dist_ = numpy.linalg.norm(i - d_test)
                dist.append(dist_)
        #print("x = " + str(x[0]) + " y = " + str(y[0]))
        # 候选人名单
        candidate = ['Obama', 'Ligengxi', 'Wangshixian', 'wzh']
        # 候选人和距离组成一个dict
        c_d = dict(zip(candidate, dist))
        cd_sorted = sorted(c_d.items(), key=lambda d: d[1])
        if (len(x) == 0):
            continue
        else:
            print(str(count) + ': The person is: %s'% (cd_sorted[0][0]) + ' x = ' + str(x[0]) + ' y = '+ str(y[0]) )

    count = count + 1
    #print(count)
    # 显示图像并等待10毫秒按键输入，输入‘q’退出程序
#     cv2.imshow(0, frame)
#     c = cv2.waitKey(10)
#     if c & 0xFF == ord('q'):
#         break
#
# # 释放摄像头并销毁所有窗口
# cap.release()
# cv2.destroyAllWindows()


# img = io.imread(img_path)
# dets = detector(img, 1)
# dist = []
# ii = 0
# x = []
# y = []
# for k, d in enumerate(dets):
#     shape = sp(img, d)
#     face_descriptor = facerec.compute_face_descriptor(img, shape)
#     d_test = numpy.array(face_descriptor)
#     x.append(int((d.right() + d.left()) / 2))
#     y.append(d.bottom())
#     # 计算欧式距离
#     for i in descriptors:
#         dist_ = numpy.linalg.norm(i - d_test)
#         dist.append(dist_)
# print("x = " + str(x[0]) + " y = " + str(y[0]))
# # 候选人名单
# candidate = ['Obama', 'Ligengxi', 'Wangshixian', 'wzh']
# # 候选人和距离组成一个dict
# c_d = dict(zip(candidate, dist))
# cd_sorted = sorted(c_d.items(), key=lambda d: d[1])
# print('The person is: %s' % (cd_sorted[0][0]))
