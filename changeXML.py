# -*- coding: UTF-8 -*-
import os
import os.path
from xml.etree.ElementTree import parse, Element


path = "D:/image/image_0304/Annotation/All"
savepath = "D:/image/XML_0304"
files = os.listdir(path)  # 得到文件夹下所有文件名称

for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

    path = "D:/image/image_0304/Annotation/All"
    newStr = os.path.join(path, xmlFile)
    dom = parse(newStr)  ###最核心的部分,路径拼接,输入的是具体路径
    root = dom.getroot()

    if xmlFile[0:9] =='Black_Tea':
        root[2][1].text = "Black Tea"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:6] =='Cheers':
        root[2][1].text = "Cheers"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:11] =='Coffee_Milk':
        root[2][1].text = "Coffee Milk"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:9] =='Crunchoco':
        root[2][1].text = "Crunchoco"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:12] =='Family_Water':
        root[2][1].text = "Family Water"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:14] =='Green_Milk_Tea':
        root[2][1].text = "Green Milk Tea"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:4] =='Lays':
        root[2][1].text = "Lays"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:9] =='Lemon_Tea':
        root[2][1].text = "Lemon Tea"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:5] =='Lotte':
        root[2][1].text = "Lotte"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:4] =='LP33':
        root[2][1].text = "LP33"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:10] =='LS_Soymilk':
        root[2][1].text = "LS Soymilk"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:10] =='Oats_Drink':
        root[2][1].text = "Oats Drink"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:11] =='Ocean_Spray':
        root[2][1].text = "Ocean Spray"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:15] =='Oolong_Milk_Tea':
        root[2][1].text = "Oolong Milk Tea"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:4] =='Oreo':
        root[2][1].text = "Oreo"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:4] =='Puff':
        root[2][1].text = "Puff"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:6] =='Purple':
        root[2][1].text = "Purple"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:8] =='Soy_Oats':
        root[2][1].text = "Soy Oats"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:7] =='Soymilk':
        root[2][1].text = "Soymilk"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')
    if xmlFile[0:11] =='With_Kernel':
        root[2][1].text = "With Kernel"
        saveStr = os.path.join(savepath, xmlFile)
        dom.write(saveStr, xml_declaration=False, encoding='utf-8')


# 作者：giveMakeMeHappy
# 链接：https: // www.jianshu.com / p / cf12bef0872c
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。