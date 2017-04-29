# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class tansuoSigleTests(ContactsAndroidTests):
    def test_4_jie_jie_tu_po(self):
        loggerInner.info("------start level fight tasks !!")
        start2TingYuan(self.driver)
        #点击探索探索
        loggerInner.info("------click search button at {x},{y} ".format(x=int(XMAX*53/100),y=int(YMAX/5)))
        self.driver.tap([(int(XMAX*53/100),int(YMAX/5))])
        sleep(15)
        self.jie_jie_tu_po()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(tansuoSigleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

