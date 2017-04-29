# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class allTests(ContactsAndroidTests):
    ######这里是最开始的几个测试用例，后来分离到了单个用例里面去了


    def test_3_yu_hun(self):
        loggerInner.info("------start yu hun!! ")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(5)
        self.yu_hun(count=3)
    def test_2_jue_xing(self):
        loggerInner.info("------start jue xing !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button in tingyuan at {x},{y}".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(5)
        self.jue_xing(type='shui',count=3)
    def test_1_tan_suo_fu_ben(self):
        loggerInner.info("------start level fight tasks !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(5)
        self.tan_suo(count=3)

    def test_4_jie_jie_tu_po(self):
        loggerInner.info("------start jiejietupo fight tasks !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(15)
        self.jie_jie_tu_po()
    def test_5_you_qing(self):
        loggerInner.info("------start get you qing task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")
        self.you_qing()
    def test_6_jie_jie_set(self):
        loggerInner.info("------start get you qing task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")
        self.jie_jie_jingyan()
    def test_7_update_yu_hun(self):
        loggerInner.info("------start get you qing task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")
        self.update_yu_hun()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(allTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

