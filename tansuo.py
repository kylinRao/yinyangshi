# coding=utf-8
import sys

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class juexingTests(ContactsAndroidTests):
    def test_1_tan_suo_fu_ben(self):
        count = 3
        try:
            if sys.argv[1]:

                count = sys.argv[1]
                print "count is {count}".format(count=count)
        except:
                pass

        loggerInner.info("------start level fight tasks !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(5)
        self.tan_suo(count=count)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(juexingTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

