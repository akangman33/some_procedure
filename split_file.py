# -*- coding: UTF-8 -*-
import os
import random
import shutil

imgpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\image"
xmlpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\xml"
train_imgpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\train_image"
test_imgpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\test_image"
train_xmlpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\train_xml"
test_xmlpath = "C:\\Users\\kevinchen19040\\Downloads\\downloads\\test_xml"

def moveFile(imgDir,xmlDir,trainImgDir,testImgDir,trainXmlDir,testXmlDir,n):
    if not os.path.exists(imgDir):
        print(imgDir+"資料夾不存在!")
    if not os.path.exists(xmlDir):
        print(xmlDir+"資料夾不存在!")
    if not os.path.exists(trainImgDir):
        print(trainImgDir+"目的資料夾不存在!\n正在新建資料夾...")
        os.mkdir(trainImgDir)
    if not os.path.exists(testImgDir):
        print(testImgDir+"目的資料夾不存在!\n正在新建資料夾...")
        os.mkdir(testImgDir)
    if not os.path.exists(trainXmlDir):
        print(trainXmlDir+"目的資料夾不存在!\n正在新建資料夾...")
        os.mkdir(trainXmlDir)
    if not os.path.exists(testXmlDir):
        print(testXmlDir+"目的資料夾不存在!\n正在新建資料夾...")
        os.mkdir(testXmlDir)
    else:
        print("正在清空資料夾")
        shutil.rmtree(trainImgDir)
        os.mkdir(trainImgDir)
        shutil.rmtree(testImgDir)
        os.mkdir(testImgDir)
        shutil.rmtree(trainXmlDir)
        os.mkdir(trainXmlDir)
        shutil.rmtree(testXmlDir)
        os.mkdir(testXmlDir)

    pathDir = os.listdir(imgDir)
    sample = random.sample(pathDir, n)
    print("正在隨機移動檔案。。。。")

    for name in sample:
        print(name)
        shutil.move(imgDir + '\\' + name, testImgDir + '\\' + name)
        xmlname = name.replace("jpg", "xml")
        shutil.move(xmlDir + '\\' + xmlname, testXmlDir + '\\' + xmlname)
    print("test檔案隨機移動完成！\n")

    pathImgDir = os.listdir(imgDir)
    for name in pathImgDir:
        shutil.move(imgDir + '\\' + name, trainImgDir + '\\' + name)
    pathXmlDir = os.listdir(xmlDir)
    for name in pathXmlDir:
        shutil.move(xmlDir + '\\' + name, trainXmlDir + '\\' + name)
    print("train檔案隨機移動完成！\n")

def visitDir(path):
    fileNum = 0
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum +1
    testNum = fileNum*0.1   #隨機選擇10%測試檔案
    print('總共', fileNum, ' 檔案') # 統計檔案數量
    print('隨機選擇', testNum, '檔案')
    return int(testNum)

moveFile(imgpath, xmlpath, train_imgpath, test_imgpath,
         train_xmlpath, test_xmlpath, visitDir(imgpath))
print("檔案隨機移動完成！\n")