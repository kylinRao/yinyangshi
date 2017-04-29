# coding=utf-8
import time
from siftxy import *
from conf.globalFacts import *
from PIL import  Image
from conf.globalFacts import *


def start2TingYuan(driver):
    time.sleep(15)


    #所有前提的开始会进行一次更新检测操作，如果检测到更新，那么我们选择更新，并且等地啊1min，检查更新并且等待更新完毕
    loggerInner.info("------check if there is a updating page!!")
    try:
        time.sleep(10)
        driver.get_screenshot_as_file(defaultSSPath)
        x,y = get_x_y(defaultSSPath,shengjiConfirmButton,0.1)
        if x != "nox":
            driver.tap([(x,y)])
            time.sleep(30)
            driver.tap([(1,1)])
            time.sleep(30)
            driver.tap([(1,1)])
            time.sleep(40)
    except:
        loggerInner.error("some error in check update action!")
        pass







    #等待10s中，可以看到视频加载出来了，我们点击下视频任意位置，进入可能存在的公告页面
    loggerInner.info("------wait for 10s to go through a game video")

    time.sleep(5)
    driver.tap([(XMAX/2,YMAX*3/4)])


    loggerInner.info("------check if there is a notice page!!")
    try:
        time.sleep(8)
        driver.get_screenshot_as_file(defaultSSPath)
        x,y = get_x_y(defaultSSPath,noticeCloseButtonColor,0.1)
        if x != "nox":
            driver.tap([(x,y)])

    except:
        loggerInner.error("some error in check notice action!")
        pass


    time.sleep(6)
    #接下来就是等待进入游戏四个大字出现在中下方了
    loggerInner.info("------wait for 11s and click {x},{y} to click entry of the game!!".format(x=XMAX/2,y=YMAX*3/4))
    time.sleep(11)
    driver.tap([(XMAX/2,YMAX*3/4)])
    #点击完进入游戏我们还会进入到一个四大主角集合照，随便点击一个位置，可以进入到下一幕
    loggerInner.info("------wait for 25s and click {x},{y} to go through 4 role photo".format(x=XMAX/2,y=YMAX*3/4))
    time.sleep(25)
    driver.tap([(XMAX/2,YMAX*3/4)])

    #到此位置按常理我们就到了庭院了，但是有时候我们会被弹出来的公告打搅，因为我们需要判断是否存在公告，存在的话我们需要关闭它，然后切回到庭院的主视图
    time.sleep(6)

    try:
        loggerInner.info("-----sleep 18s, and check for notice!!at tingyuan !!")
        time.sleep(18)
        driver.get_screenshot_as_file(defaultSSPath)

        x,y = get_x_y(defaultSSPath,noticeCloseButton)


        loggerInner.info("-----get close button at {x},{y} !!".format(x=x,y=y))
        if x != "nox":
            driver.tap([(x,y)])
            loggerInner.info("------there is a notice ,and we click {x},{y} to close the notice !".format(x=XMAX*95/100,y=YMAX/2))
            driver.tap([(int(XMAX*95/100),int(YMAX/2))])



    except:
        loggerInner.debug("------check notice error!!")
        time.sleep(25)
        driver.get_screenshot_as_file(defaultSSPath)

        x,y = get_x_y(defaultSSPath,noticeCloseButton,0.1)
        if x != "nox":
            driver.tap([(x,y)])
            loggerInner.info("------there is a notice ,and we click {x},{y} to close the notice !".format(x=XMAX*95/100,y=YMAX/2))
            driver.tap([(int(XMAX*95/100),int(YMAX/2))])
    loggerInner.info("------sleep 10s and we entered tingyuan and click search entry!!----")
    time.sleep(10)


