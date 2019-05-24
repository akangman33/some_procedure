import xml.etree.ElementTree as ET
import pickle
import os
from os import getcwd
import numpy as np
from PIL import Image

import imgaug as ia
from imgaug import augmenters as iaa

ia.seed(1)

def read_xml_annotation(root, image_id):
    in_file = open(os.path.join(root, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    bndboxlist = []

    for object in root.findall('object'):  # 找到root節點下的所有country節點
        bndbox = object.find('bndbox')  # 子節點下節點rank的值

        xmin = int(bndbox.find('xmin').text)
        xmax = int(bndbox.find('xmax').text)
        ymin = int(bndbox.find('ymin').text)
        ymax = int(bndbox.find('ymax').text)
        # print(xmin,ymin,xmax,ymax)
        bndboxlist.append([xmin,ymin,xmax,ymax])
        # print(bndboxlist)

    bndbox = root.find('object').find('bndbox')
    return bndboxlist
# (506.0000, 330.0000, 528.0000, 348.0000) -> (520.4747, 381.5080, 540.5596, 398.6603)
def change_xml_annotation(root, image_id, new_target):
    new_xmin = new_target[0]
    new_ymin = new_target[1]
    new_xmax = new_target[2]
    new_ymax = new_target[3]

    in_file = open(os.path.join(root, str(image_id) + '.xml'))  # 這裡root分别由兩個意思
    tree = ET.parse(in_file)
    xmlroot = tree.getroot()
    object = xmlroot.find('object')
    bndbox = object.find('bndbox')
    xmin = bndbox.find('xmin')
    xmin.text = str(new_xmin)
    ymin = bndbox.find('ymin')
    ymin.text = str(new_ymin)
    xmax = bndbox.find('xmax')
    xmax.text = str(new_xmax)
    ymax = bndbox.find('ymax')
    ymax.text = str(new_ymax)
    tree.write(os.path.join(root, str(image_id) + "_aug" + '.xml'))

def change_xml_list_annotation(root, image_id, new_target, saveroot, id, height, width):

    in_file = open(os.path.join(root, str(image_id) + '.xml'))  # 這裡root分别由兩個意思
    tree = ET.parse(in_file)
    xmlroot = tree.getroot()
    index = 0

    for object in xmlroot.findall('object'):  # 找到root節點下的所有country節點
        bndbox = object.find('bndbox')  # 子節點下節點rank的值

        # xmin = int(bndbox.find('xmin').text)
        # xmax = int(bndbox.find('xmax').text)
        # ymin = int(bndbox.find('ymin').text)
        # ymax = int(bndbox.find('ymax').text)

        new_xmin = new_target[index][0]
        new_ymin = new_target[index][1]
        new_xmax = new_target[index][2]
        new_ymax = new_target[index][3]

        if new_xmin < 0 or new_ymin < 0 or new_xmax > width or new_ymax > height:
            print(new_xmin, new_ymin, new_xmax, new_ymax)
            xmlroot.remove(object)
        else:
            xmin = bndbox.find('xmin')
            xmin.text = str(new_xmin)
            ymin = bndbox.find('ymin')
            ymin.text = str(new_ymin)
            xmax = bndbox.find('xmax')
            xmax.text = str(new_xmax)
            ymax = bndbox.find('ymax')
            ymax.text = str(new_ymax)

        index = index + 1

    tree.write(os.path.join(saveroot, str(image_id) + "_aug_" + str(id) + '.xml'))


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符號
    path = path.rstrip("\\")
    # 判斷路徑是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断結果
    if not isExists:
        # 如果不存在則創建目錄
        # 創建目錄操作函數
        os.makedirs(path)
        print(path + ' 創建成功')
        return True
    else:
        # 如果目錄存在則不創建，並提示目錄已存在
        print(path + ' 目錄已存在')
        return False

if __name__ == "__main__":

    IMG_DIR = "../test4"
    XML_DIR = "../xml4"

    AUG_XML_DIR = "../AUG_XML"  # 存儲增強後的XML文件夾路徑
    mkdir(AUG_XML_DIR)

    AUG_IMG_DIR = "../AUG_IMG"  # 存儲增强後的影像文件夾路徑
    mkdir(AUG_IMG_DIR)

    AUGLOOP = 10  # 每張影像增强的數量

    boxes_img_aug_list = []
    new_bndbox = []
    new_bndbox_list = []


    # 影像增强
    matrix = np.array([[0, -4, 0],
                       [-4, 16, -4],
                       [0, -4, 0]])
    seq = iaa.Sequential([
        # iaa.Flipud(1),  # vertically flip 20% of all images，垂直翻轉
        # iaa.Fliplr(0.5),  # 鏡像，水平翻轉
        # iaa.Multiply((0.5, 1.2)),  # change brightness, doesn't affect BBs，亮暗
        # iaa.GaussianBlur(sigma=(0, 3.0)), # iaa.GaussianBlur(0.5),
        # iaa.Affine(
        #     translate_px={"x": 15, "y": 15},
        #     scale=(0.95, 1.3),
        #     rotate=(-25, 25)
        # )  # translate by 40/60px on x/y axis, and scale to 50-70%, affects BBs
        # iaa.WithColorspace(
        #     to_colorspace="HSV",
        #     from_colorspace="RGB",
        #     children=iaa.WithChannels([0,1,2], iaa.Add((10, 50)))
        # )
        # iaa.WithChannels(2, iaa.Add((10, 100)))
        # iaa.Sequential([
        #     iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
        #     iaa.WithChannels(0, iaa.Add((50, 100))),
        #     iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
        # ])
        # iaa.Grayscale(alpha=(0.0, 1.0))
        # iaa.GaussianBlur(sigma=3.0)
        # iaa.AverageBlur(k=(2, 11))
        # iaa.AverageBlur(k=((5, 11), (1, 3)))
        # iaa.MedianBlur(k=(3, 11))
        # iaa.Convolve(matrix=matrix)
        # iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
        # iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5))
        # iaa.EdgeDetect(alpha=(0.0, 1.0))
        # iaa.DirectedEdgeDetect(alpha=(0.0, 1.0), direction=(0.0, 1.0))
        # iaa.Add((-40, 40), per_channel=0.5)
        # iaa.AddElementwise((-40, 40), per_channel=0.5)
        # iaa.AdditiveGaussianNoise(scale=0.05 * 255, per_channel=0.5)
        # iaa.Multiply((0.5, 1.5), per_channel=0.5)
        # iaa.MultiplyElementwise((0.5, 1.5), per_channel=0.5)
        # iaa.Dropout(p=(0, 0.2), per_channel=0.5)
        # iaa.CoarseDropout((0.0, 0.05), size_percent=(0.02, 0.25))
        # iaa.CoarseDropout(0.02, size_percent=0.15, per_channel=0.5)
        # iaa.Invert(0.25, per_channel=0.5)
        # iaa.ContrastNormalization((0.5, 1.5), per_channel=0.5)
        # iaa.PiecewiseAffine(scale=(0.01, 0.05))
        iaa.ElasticTransformation(alpha=(0, 5.0), sigma=0.25)
    ])

    for root, sub_folders, files in os.walk(XML_DIR):

        for name in files:

            bndbox = read_xml_annotation(XML_DIR, name)

            for epoch in range(AUGLOOP):
                seq_det = seq.to_deterministic()  # 保持座標和圖像同步改變，而不是随機

                # 讀取圖片
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.jpg'))
                img = np.array(img)
                height = img.shape[0]
                width = img.shape[1]

                # bndbox 座標增強
                for i in range(len(bndbox)):
                    bbs = ia.BoundingBoxesOnImage([
                        ia.BoundingBox(x1=bndbox[i][0], y1=bndbox[i][1], x2=bndbox[i][2], y2=bndbox[i][3]),
                    ], shape=img.shape)

                    bbs_aug = seq_det.augment_bounding_boxes([bbs])[0]
                    boxes_img_aug_list.append(bbs_aug)

                    # new_bndbox_list:[[x1,y1,x2,y2],...[],[]]
                    new_bndbox_list.append([int(bbs_aug.bounding_boxes[0].x1),
                                            int(bbs_aug.bounding_boxes[0].y1),
                                            int(bbs_aug.bounding_boxes[0].x2),
                                            int(bbs_aug.bounding_boxes[0].y2)])
                # 存儲變化後的圖片
                image_aug = seq_det.augment_images([img])[0]
                path = os.path.join(AUG_IMG_DIR, str(name[:-4]) + "_aug_" + str(epoch) + '.jpg')
                image_auged = bbs.draw_on_image(image_aug, size=0)
                Image.fromarray(image_auged).save(path)

                # 存儲變化後的XML
                change_xml_list_annotation(XML_DIR, name[:-4], new_bndbox_list, AUG_XML_DIR, epoch, height, width)
                print(str(name[:-4]) + "_aug_" + str(epoch) + '.jpg')
                new_bndbox_list = []

