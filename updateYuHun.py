
# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class sigleTests(ContactsAndroidTests):
    def test_7_update_yu_hun(self):
        loggerInner.info("------start get you qing task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")
        self.update_yu_hun()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(sigleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

