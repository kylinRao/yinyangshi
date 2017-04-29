# coding=utf-8
import  time

import numpy as np
from PIL import Image

from conf.globalFacts import *


# import matplotlib.pyplot as plt


# 打开图像并转化为数字矩阵

#print img
#3print len(img)
#print img[1]
#该函数通过输入两张图片的文件位置，定位出小图片在大图片中的xy坐标，并返回给调用方
def find_pix_x_y(BigPicPath,SmallPicPath):
    print time.time()
    print "{datu} and {xiaotu}".format(datu=BigPicPath,xiaotu=SmallPicPath)

    imgDa = np.array(Image.open(BigPicPath))
    imgXiao = np.array(Image.open(SmallPicPath))

    imgDaList = imgDa.tolist()
    imgXiaoList = imgXiao.tolist()
    #print "imgDaList:",imgDaList
    # with open("a.txt",'w') as f:
    #     print >> f,imgDaList

    print "imgXiaoList:",imgXiaoList[0]
    imgXiaoEveryLineLenth = len(imgXiaoList[0])
    for imgDaListEveryLine in imgDaList:
        y = 666666
        x = 666666
        for list in imgDaListEveryLine:
            if imgXiaoList[0][0][2] == list[2]:


            #if imgXiaoList[0][0] in imgDaListEveryLine:
               # print "i find you ",imgDaListEveryLine

                fy = imgDaList.index(imgDaListEveryLine)
                fx = imgDaListEveryLine.index(list)

                for i in range(0,imgXiaoEveryLineLenth):
                    print i

                    if imgDaListEveryLine[fx+i][2] == imgXiaoList[0][i][2]:

                        if i == imgXiaoEveryLineLenth-1:
                            y = fy
                            x = fx + + imgXiaoEveryLineLenth/2
                            print "it is {x},{y}".format(x = x,y = y)
                            return  x,y
                    if imgDaListEveryLine[fx+i][2] != imgXiaoList[0][i][2]:
                        if fx + i == XMAX -1:
                            break
                        #print "{a} not equel {b},in index {j},{i}".format(a = imgDaListEveryLine[fx+i],b = imgXiaoList[0][i],j = fy,i = fx+i)
                        break





    print "x and y is:",x,y
    return x,y

if __name__ == '__main__':
    x,y = find_pix_x_y('screenshot.png','tansuo_xiaobing_wuhuangguang.png')
    print x,y


