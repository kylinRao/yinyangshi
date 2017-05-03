# coding=utf-8
import os
from conf.globalFacts import  *
import unittest
from time import sleep

from appium import webdriver


#from juzhen import  *

from siftxy import *
from start2tingyuan import  *
from senceCheck import  *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def add_10_food(self):
        #点击卷轴
        loggerInner.info("----open the rolled book!!")
        self.driver.tap([(int(XMAX*95/100),int(YMAX*85/100))])
        sleep(3)
        #点击阴阳寮
        loggerInner.info("----enter commity!!")
        self.driver.tap([(int(XMAX*30/100),int(YMAX*85/100))])
        sleep(8)
        #点击地图
        loggerInner.info("----click the map!!")


        self.driver.tap([(int(XMAX*85/100),int(YMAX*85/100))])
        sleep(30)
        count = 0
        x = "nox"
        while (x == "nox"):
            count  = count + 1
            loggerInner.info("-----this is the {count} time to find food pic".format(count=count))
            self.shot_screen()
            x,y = get_x_y(defaultSSPath,food)
            if count == 30:
                break
        self.driver.tap([(x,y)])
        sleep(3)
        self.shot_screen()
        x,y = get_x_y(defaultSSPath,buji)
        self.driver.tap([(x,y)])
        sleep(5)
        loggerInner.info("----get 10 succi successfully!!!")
    def jie_jie_tu_po(self):
        loggerInner.info("------enter jiejietupo  at {x},{y} ".format(x=XMAX*3/10,y=YMAX*9/10))
        self.driver.tap([(int(XMAX*3/10),int(YMAX*9/10))])
        sleep(10)
        loggerInner.info("------refresh jiejietupo  at {x},{y} ".format(x=XMAX*3/10,y=YMAX*9/10))
        self.driver.tap([(int(XMAX*8/10),int(YMAX*75/100))])
        sleep(5)

        loggerInner.info("------refresh confirm  at {x},{y} ".format(x=XMAX*6/10,y=YMAX*6/10))
        self.driver.tap([(int(XMAX*6/10),int(YMAX*6/10))])
        sleep(5)

        xlist = [int(XMAX*2/10),int(XMAX*5/10),int(XMAX*8/10)]
        ylist = [int(YMAX*2/10),int(YMAX*4/10),int(YMAX*6/10)]
        xylist = []
        for x in xlist:
            for y in ylist:
                xylist.append((x,y))
        count = 9
        for point in xylist:

            self.driver.tap([point])
            sleep(5)
            #点击攻击按钮
            self.shot_screen()
            x,y = get_x_y(defaultSSPath,attackButton)
            if x != "nox":
                loggerInner.info("------find attackButton,at {x},{y}".format(x=x,y=y))
                self.driver.tap([(x,y)])
            sleep(20)
            #点击开始战斗
            loggerInner.info("------now count={count}，click fight begin button  at {x},{y}!! ".format(count=count,x=int(XMAX*9/10),y=int(YMAX*8/10)))
            sleep(8)
            self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
            sleep(8)
            self.shot_screen()
            sences =  [

                {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

                {"sence": SenceVictory, "path": SenceFlagSenceVictory},
                {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

            ]
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                pass
            elif sence == SenceVictory:
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])

            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1
            if count <=0:
                break




    def get_five_point_lists(self,x,y):
        fivePointList01 = [(x,y)]
        if 0 < x-XMAX/20  :
            fivePointList01.append((int(x-XMAX/20),y))
        if  x+XMAX/20<XMAX:
            fivePointList01.append((int(x+XMAX/20),y))
        if int(YMAX*15/100)<y-YMAX/20:
            fivePointList01.append((x,int(y-YMAX/20)))
        if y+YMAX/20 < YMAX:
            fivePointList01.append((x,int(y+YMAX/20)))

        for ll in fivePointList01:
            loggerInner.info("-----five points contain {x},{y}".format(x=ll[0],y=ll[1]))

        fivePointList02 = [(x,y)]
        ###两种触摸点扩张方案，优先使用上下左右扩张方案
        #再次扩大一圈范围获得5个点

        if 0 < x-XMAX/10  :
            fivePointList02.append((int(x-XMAX/10),y))
        if  x+XMAX/10<XMAX:
            fivePointList02.append((int(x+XMAX/10),y))
        if int(YMAX*15/100)<y-YMAX/10:
            fivePointList02.append((x,int(y-YMAX/10)))
        if y+YMAX/10 < YMAX:
            fivePointList02.append((x,int(y+YMAX/10)))




        fivePointList03 = [(x,y)]
        #再次扩大一圈范围获得5个点
        if 0 < x-XMAX/5  :
            fivePointList03.append((int(x-XMAX/5),y))
        if  x+XMAX/5<XMAX:
            fivePointList03.append((int(x+XMAX/5),y))
        if int(YMAX*15/100)<y-YMAX/5:
            fivePointList03.append((x,int(y-YMAX/5)))
        if y+YMAX/5 < YMAX:
            fivePointList03.append((x,int(y+YMAX/5)))

        fivePointList04 = [(x,y)]
        if (0 < x-XMAX/10) and (int(YMAX*15/100)<y-YMAX/10)  :
            fivePointList04.append((int(x-XMAX/10),int(y-YMAX/10)))
        if  (x+XMAX/10<XMAX) and (int(YMAX*15/100)<y-YMAX/10):
            fivePointList04.append((int(x+XMAX/10),int(y-YMAX/10)))
        if (x+XMAX/10 < XMAX) and (y+YMAX/10<YMAX) :
            fivePointList04.append((int(x+XMAX/10),int(y+YMAX/10)))
        if (0 < x-XMAX/10) and (y+YMAX/10 < YMAX)  :
            fivePointList04.append((int(x-XMAX/10),int(y+YMAX/10)))

        fivePointList05 = [(x,y)]
        if (0 < x-XMAX/5) and (int(YMAX*15/100)<y-YMAX/5)  :
            fivePointList05.append((int(x-XMAX/5),int(y-YMAX/5)))
        if  (x+XMAX/5<XMAX) and (int(YMAX*15/100)<y-YMAX/5):
            fivePointList05.append((int(x+XMAX/5),int(y-YMAX/5)))
        if (x+XMAX/5 < XMAX) and (y+YMAX/5<YMAX) :
            fivePointList05.append((int(x+XMAX/5),int(y+YMAX/5)))
        if (0 < x-XMAX/5) and (y+YMAX/5 < YMAX)  :
            fivePointList05.append((int(x-XMAX/5),int(y+YMAX/5)))


        return [fivePointList05,fivePointList04,fivePointList03,fivePointList02,fivePointList01]

    def yu_hun(self,type='yuhun',count = 3):
        starttime = time.time()
        #每一个count给5min，就是300s
        presettime = 300*count
        type = yunHunPath

        self.shot_screen()

        #点击御魂入口
        loggerInner.info("------click yu hun entry!! ")
        self.driver.tap([(int(XMAX*16/100),int(YMAX*95/100))])


        sleep(3)
        loggerInner.info("------click big snack at {x},{y}!! ".format(x=XMAX/4,y=YMAX/2))
        self.driver.tap([(XMAX/4,YMAX/2)])

        sleep(3)
        #点击挑战button
        loggerInner.info("------click yu hun fight entry button at {x},{y}!! ".format(x=int(XMAX*3/4),y=int(YMAX*7/10)))
        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])



        while count >= 1:
            loggerInner.info("------now count={count}，that means {count} times should be tried again!! ".format(count=count))
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            sleep(3)
            #点击挑战按钮
            loggerInner.info("------now count={count}，click fight start entry button  at {x},{y}!! ".format(count=count,x=int(XMAX*3/4),y=int(YMAX*7/10)))
            self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
            #点击开始战斗
            loggerInner.info("------now count={count}，click fight begin button  at {x},{y}!! ".format(count=count,x=int(XMAX*9/10),y=int(YMAX*8/10)))
            sleep(3)
            self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
            sences =  [

        {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

        {"sence": SenceVictory, "path": SenceFlagSenceVictory},
        {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

    ]
            self.shot_screen()
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1
            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1

    def jue_xing(self,type="lei",count=3):

        self.shot_screen()
        #点击觉醒入口
        self.driver.tap([(int(XMAX*8/100),int(YMAX*93/100))])
        #选择任意一个麒麟
        sleep(3)
        if type=="huo":
            self.driver.tap([(XMAX/5,YMAX/2)])
        if type=="feng":
            self.driver.tap([(XMAX*2/5,YMAX/2)])
        if type=="shui":
            self.driver.tap([(XMAX*3/5,YMAX/2)])
        if type=="lei":
            self.driver.tap([(XMAX*4/5,YMAX/2)])

        sleep(3)
        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
        starttime = time.time()
        #每一个count给5min，就是300s
        presettime = 300*count



        while count >= 1:
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            sleep(3)
            #点击挑战按钮
            self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
            #点击开始战斗
            sleep(3)
            self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
            sences =  [

        {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

        {"sence": SenceVictory, "path": SenceFlagSenceVictory},
        {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

    ]

            self.shot_screen()
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1
            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                count = count - 1

    def shot_screen_backup(self):
        #这个函数截取出来的图片是横屏的图片
        #sleep(1)
        self.driver.get_screenshot_as_file("screenshotPre.png")

        img = Image.open("screenshotPre.png")
        img2 = img.transpose(Image.ROTATE_270)
        img2.save(defaultSSPath)
    def shot_screen(self):
        #这个函数截图出来的图片是竖屏的图片，为了保证响应速度，我们使用这个函数来配合图片识别操作的函数（也就是siftxy.py里面的函数，对应的x,y返回结果时，我们也做了相关的线性变化）
        #sleep(1)
        self.driver.get_screenshot_as_file(defaultSSPath)

    def tan_suo(self,count=1,level=tanSuoLevel13Path):
        starttime = time.time()
        #每一个count给15min，就是900s
        presettime = 900*count


        loggerInner.info("------enter fight level  at {x},{y} ".format(x=XMAX*9/10,y=YMAX/2))
        self.driver.tap([(XMAX*9/10,int(YMAX/4))])
        sleep(6)
        #点击探索button，进入选择小怪页面
        loggerInner.info("------click level fight entry button at {x},{y} ".format(x=int(XMAX*3/4),y=int(YMAX*7/10)))

        self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
        sleep(6)




        #我们一共需要打三次副本

        #步数计数，四步右来四步左
        step = 0
        #方向标志位
        direction = 1
        while count >= 0:
            timenow = time.time()
            if (timenow - starttime)> presettime:
                break
            self.shot_screen()
            sence = get_sence(defaultSSPath)
            loggerInner.info("------now sence is {sence}".format(sence=sence))
            if sence == SenceTanSuoFuBenXuanZe:
                #只进行妖怪打斗标志检索，检索完了点击。如果检索不到就往右移动半屏幕(四次之后改变方向移动四次)，再次检索。
                self.shot_screen()
                x,y = get_x_y(defaultSSPath,SenceBossFightPic)
                if x != "nox":
                    loggerInner.info("------find boss,at {x},{y}".format(x=x,y=y))
                    self.driver.tap([(x,y)])

                self.shot_screen()
                x,y = get_x_y(defaultSSPath,tanSuoZhunBeiPath)
                if x != "nox":
                    loggerInner.info("------find an small demo,at {x},{y}".format(x=x,y=y))
                    fivePointList = self.get_five_point_lists(x,y)
                    for index in range(0,len(fivePointList)):
                        self.driver.tap(fivePointList[index])
                    #检查下是否有战斗开始的开关，因为有时候会忘记开锁定式神的功能
                    loggerInner.info("------now count={count}，click fight begin button  at {x},{y}!! ".format(count=count,x=int(XMAX*9/10),y=int(YMAX*8/10)))
                    sleep(8)
                    self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])




                    sleep(3)

                else:
                    #没找到妖怪的话有可能是发现大boss了（或者打完boss掉落好东西了），也有可能真的没发现任何人，我们就要走两步了去找妖怪去
                    #判断如果有boss，就打boss
                    self.shot_screen()

                    x,y = get_x_y(defaultSSPath,bossJiangpinButton)
                    if x != "nox":
                        loggerInner.info("------after boss fight ,there is some trasures,at {x},{y}".format(x=x,y=y))
                        self.driver.tap([(x,y)])
                    step = direction + step
                    if step > 0:
                        loggerInner.info("------step right forward")
                        self.driver.tap([(XMAX-1,int(YMAX*2/3))])
                        sleep(6)
                        if step >= 4:
                            step = 0
                            direction = -direction
                    elif step < 0:
                        loggerInner.info("------step left forward")
                        self.driver.tap([(1,int(YMAX*2/3))])
                        sleep(6)
                        if step <= -4:
                            step = 0
                            direction = -direction




            elif sence == SenceTanSuoFuBenFighting:
                #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                loggerInner.info("------get fight level  at {x},{y} ".format(x=XMAX*9/10,y=YMAX/2))
                self.driver.tap([(XMAX*9/10,YMAX/2)])
                sleep(6)
                #点击探索button，进入选择小怪页面
                loggerInner.info("------click level fight entry button at {x},{y} ".format(x=int(XMAX*3/4),y=int(YMAX*7/10)))

                self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
                sleep(6)

                x,y=get_x_y(defaultSSPath,fuBenTanSuoKaiShiButton,accurate=0.1)
                if x != "nox":
                    self.driver.tap([(x,y)])

                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictory:
                loggerInner.info("------fight ends,receive your rewards!----")
                #探测到战斗成页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == SenceVictoryDaMo:
                loggerInner.info("------fight ends,receive your rewards!damo----")
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(3)
                self.driver.tap([(XMAX/2,YMAX/2)])

            elif sence == SenceTanSuoFuBenHomePage:
                self.shot_screen()
                #先判断下有没有宝箱可以领取，如果有的话不要忘记领取了
                x,y = get_x_y(defaultSSPath,baoXiang)
                if x != "nox":
                    self.driver.tap([(x,y)])
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
                #探测到探索关卡选择页面，我们先找到需要打的关卡，进入后，点击开始探索按钮即可

                x,y = get_x_y(defaultSSPath,level)
                loggerInner.info("------get fight level at {x},{y}".format(x=x,y=y))
                self.driver.tap([(x,y)])
                sleep(5)
                self.driver.tap([(int(XMAX*3/4),int(YMAX*7/10))])
                sleep(3)
                count = count - 1


    #友情点获取
    def you_qing(self):
        #点击卷轴
        loggerInner.info("----open the rolled book!!")
        self.driver.tap([(int(XMAX*95/100),int(YMAX*85/100))])
        sleep(3)
        #点击好友入口
        loggerInner.info("----enter friend commity!!")
        self.driver.tap([(int(XMAX*65/100),int(YMAX*85/100))])
        sleep(8)




        #点击友情点收取或者赠送，共需要赠送5个人
        count = 4
        while count >= 0:
            self.driver.tap([(int(XMAX*35/100),int(YMAX*(35+count*13)/100))])
            sleep(4)
            self.driver.tap([(int(XMAX*35/100),int(YMAX*(35+count*13)/100))])
            sleep(4)
            count = count -1
    #获取结界经验
    def jie_jie_jingyan(self):
        #点击卷轴
        loggerInner.info("----open the rolled book!!")
        self.driver.tap([(int(XMAX*95/100),int(YMAX*85/100))])
        sleep(3)
        #点击阴阳寮
        loggerInner.info("----enter commity!!")
        self.driver.tap([(int(XMAX*30/100),int(YMAX*85/100))])
        sleep(8)
        #点击结界
        loggerInner.info("----enter jie jie!!")
        self.driver.tap([(int(XMAX*75/100),int(YMAX*90/100))])
        sleep(15)
        #不管当前有没有可收取的经验，都假装收取一次经验，一般我都会放的
        loggerInner.info("----collect experience!!")
        self.driver.tap([(int(XMAX*82/100),int(YMAX*27/100))])
        sleep(15)
    def update_yu_hun(self):
        #点击卷轴
        loggerInner.info("----open the rolled book!!")
        self.driver.tap([(int(XMAX*95/100),int(YMAX*85/100))])
        sleep(3)
        #点击式神录
        loggerInner.info("----enter shishenlu!!")
        self.driver.tap([(int(XMAX*85/100),int(YMAX*85/100))])
        sleep(8)
        #点击首个式神的详细页面
        loggerInner.info("----enter shi shen detail page!!")
        self.driver.tap([(int(XMAX*97/100),int(YMAX*55/100))])
        sleep(8)
        #点击御魂资料页面
        loggerInner.info("----enter yu hun detail page!!")
        self.driver.tap([(int(XMAX*93/100),int(YMAX*35/100))])
        sleep(8)
        #点击1号位御魂
        loggerInner.info("----click the 6 yu hun!!")
        self.driver.tap([(int(XMAX*60/100),int(YMAX*20/100))])
        sleep(8)
        #点击强化
        loggerInner.info("----click strength button page!!")
        self.driver.tap([(int(XMAX*30/100),int(YMAX*65/100))])
        sleep(8)
        #选择第一个低等级御魂
        loggerInner.info("----select the first yu hun!!")
        self.driver.tap([(int(XMAX*10/100),int(YMAX*33/100))])
        sleep(8)
        #强化
        loggerInner.info("----click strength button page!!")
        self.driver.tap([(int(XMAX*80/100),int(YMAX*90/100))])
        sleep(8)


    def yao_guai_tui_zhi(self):
        #点击町中
        loggerInner.info("----click ting zhong!!")
        self.driver.tap([(int(XMAX*58/100),int(YMAX*38/100))])
        sleep(10)
        #点击妖怪退治小灯笼
        loggerInner.info("----click yaoguaituizhi !!")
        self.driver.tap([(int(XMAX*33/100),int(YMAX*17/100))])
        sleep(10)
        #点击达摩
        loggerInner.info("----click damo !!")
        self.driver.tap([(int(XMAX*50/100),int(YMAX*50/100))])
        sleep(10)
        #点击准备按钮
        loggerInner.info("------click fight begin button !! ")


        self.driver.tap([(int(XMAX*75/100),int(YMAX*73/100))])
        sleep(8)
        #点击打架准备按钮
        loggerInner.info("------click fight begin button !! ")

        self.driver.tap([(int(XMAX*9/10),int(YMAX*8/10))])
        sleep(8)

        #进入战斗后的判断
        while 1:
            self.shot_screen()
            sences =  [

                    {"sence": SenceTanSuoFuBenFighting, "path": SenceFlagTanSuoFuBenFightingPic},

                    {"sence": SenceVictory, "path": SenceFlagSenceVictory},
                    {"sence": SenceVictoryDaMo, "path": SenceFlagVictoryDaMo},

                ]
            sence = get_sence(defaultSSPath,sences=sences)
            if sence == SenceTanSuoFuBenFighting:
                    #探测到当前在战斗画面，则每隔3s点击下中间屏幕即可
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
            elif sence == "otherSence":
                    pass
            elif sence == SenceVictory:
                    #探测到战斗成页面，点击下屏幕中间即可
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
                    sleep(3)
                    self.driver.tap([(XMAX/2,YMAX/2)])
                    sleep(5)
                    break


            elif sence == SenceVictoryDaMo:
                #探测到领取奖励页面，点击下屏幕中间即可
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(5)
                self.driver.tap([(XMAX/2,YMAX/2)])
                sleep(5)
                break

















    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '127.0.0.1:52001'
        desired_caps['appPackage'] = 'com.netease.onmyoji.huawei'
        desired_caps['appActivity'] = 'com.netease.onmyoji.Launcher'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        loggerInner.info("---------------------cases execurated!!----------------------")
        self.driver.quit()


    #######这里是最开始的几个测试用例，后来分离到了单个用例里面去了
    # def test_1_yu_hun(self):
    #     loggerInner.info("------start yu hun!! ")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.yu_hun(count=3)
    # def test_2_jue_xing(self):
    #     loggerInner.info("------start jue xing !!")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button in tingyuan at {x},{y}".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.jue_xing(type='shui',count=3)
    # def test_3_tan_suo_fu_ben(self):
    #     loggerInner.info("------start level fight tasks !!")
    #     start2TingYuan(self.driver)
    #     #点击探索探索
    #     loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
    #     self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
    #     sleep(5)
    #     self.tan_suo(count=3)












if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
