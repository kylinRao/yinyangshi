# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class sigleTests(ContactsAndroidTests):
    def test_2_jue_xing(self):

        count = 3
        type = "lei"
        try:
            if sys.argv[1]:

                count = int(sys.argv[1])
                print "count is {count}".format(count=count)
        except:
                pass
        try:
            if sys.argv[2]:

                type = sys.argv[2]
                print "type is {type}".format(type=type)
        except:
                pass
        loggerInner.info("------start jue xing !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button in tingyuan at {x},{y}".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(5)
        self.jue_xing(type=type,count=count)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(sigleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

