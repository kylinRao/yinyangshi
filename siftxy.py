#coding=utf-8
import cv2
import time
from  conf.globalFacts import *
import logging.config
import scipy as sp
def get_x_y(bigTuPath,smallTuPath,accurate=0.2):
    loggerInner.debug("screen is {screen},key shot is {ks},accurate is {accurate}".format(screen=bigTuPath,ks=smallTuPath,accurate=accurate))



    img1 = cv2.imread(bigTuPath,cv2.IMREAD_GRAYSCALE) # trainImage
    #print img1
    img2 = cv2.imread(smallTuPath,cv2.IMREAD_GRAYSCALE) # queryImage
    # Initiate SIFT detector
    sift = cv2.SIFT()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)

    search_params = dict(checks=100)   # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    #print 'matches...',len(matches)
    #print matches
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < accurate*n.distance:
            good.append(m)
   # print 'good',len(good)
    #print good
    if not good:
        return "nox","noy"
    # #####################################
    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]

    for m in good:
        # draw the keypoints
        # print m.queryIdx, m.trainIdx, m.distance
        color = tuple([sp.random.randint(0, 255) for _ in xrange(3)])
        #print 'kp1,kp2',kp1,kp2
        cv2.line(view, (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1])) , (int(kp2[m.trainIdx].pt[0] + w1), int(kp2[m.trainIdx].pt[1])), color)
        x = int(kp1[m.queryIdx].pt[0])
        y = int(kp1[m.queryIdx].pt[1])

        ##这里使用break，因为我只需要获取一个点就可以了
        break
    ###如果你想画图的话，请解开此段注释
    # cv2.imshow("view", view)
    # # cv2.waitKey()
    # print "this is like point",x,y
    # #如果发现截屏出来是竖屏的话，需要打开此项注释，调整坐标系
    # #x,y = XMAX-y,x
    # print "this is like point",x,y
    return x,y

if __name__ == '__main__':
    print time.time()
    #x,y = get_x_y(defaultSSPath,tanSuoLevel10Path)
    x,y=get_x_y(defaultSSPath,noticeCloseButton,0.1)

    print x,y