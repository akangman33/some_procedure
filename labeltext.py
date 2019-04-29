import os
import cv2
import numpy as np
import xml.dom.minidom
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

input_file = "D:/image_dataset/XML/"
dirs_name = os.listdir("D:/image_dataset/image/")  # 图片地址

font = cv2.FONT_HERSHEY_SIMPLEX
for img in dirs_name:

    im = cv2.imread("D:/image_dataset/image/" + img)  # 读取图片
    dom = xml.dom.minidom.parse(input_file + img[:-4] + ".xml")  # 读取图片对应的label信息 xml文件
    root = dom.documentElement

    objs = root.getElementsByTagName("object")

    name = []
    xmin = []
    ymin = []
    xmax = []
    ymax = []

    for obj in objs:
        name1 = obj.getElementsByTagName('name')
        n = name1[0].firstChild.data
        xmin1 = obj.getElementsByTagName('xmin')
        xi = xmin1[0].firstChild.data
        ymin1 = obj.getElementsByTagName('ymin')
        yi = ymin1[0].firstChild.data
        xmax1 = obj.getElementsByTagName('xmax')
        xa = xmax1[0].firstChild.data
        ymax1 = obj.getElementsByTagName('ymax')
        ya = ymax1[0].firstChild.data

        xmin.append(int(xi.strip()))
        print(xmin)
        ymin.append(int(yi.strip()))
        xmax.append(int(xa.strip()))
        ymax.append(int(ya.strip()))
        name.append(n.strip())

    for i in range(0, len(xmin)):
        # 画box
        cv2.rectangle(im, (xmin[i], ymin[i]), (xmax[i], ymax[i]), (0, 255, 0), 4)

    cv2img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    # 写标注
    for i in range(0, len(xmin)):
        font = ImageFont.truetype("C:/Users/Kevin/keras-yolo3/font/FiraMono-Medium.otf", 40, encoding="utf-8")
        draw.text((xmin[i], ymin[i] - 40), name[i], (255, 0, 0), font=font)

    cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

    # 保存图片
    cv2.imwrite("D:/image_dataset/label/" + img, cv2charimg)

# ---------------------
# 作者：qq_32799915
# 来源：CSDN
# 原文：https: // blog.csdn.net / qq_32799915 / article / details / 81111423
# 版权声明：本文为博主原创文章，转载请附上博文链接！