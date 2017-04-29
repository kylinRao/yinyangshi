# coding=utf-8

from testCasBase import *
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class juexingTests(ContactsAndroidTests):
    def test_10_yao_guai_tui_zhi(self):
        loggerInner.info("------start yao guai tui zhi !!")
        start2TingYuan(self.driver)

        self.yao_guai_tui_zhi()
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(juexingTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

