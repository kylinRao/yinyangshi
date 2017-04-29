# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class tansuoSigleTests(ContactsAndroidTests):
    def test_4_add_10_food(self):
        loggerInner.info("------start get food task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")


        self.add_10_food()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(tansuoSigleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

