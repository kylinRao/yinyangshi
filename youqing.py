# coding=utf-8

from testCasBase import *
import re
from multiprocessing import Process
import threading
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class sigleTests(ContactsAndroidTests):
    def test_5_you_qing(self):
        loggerInner.info("------start get you qing task !!")
        start2TingYuan(self.driver)
        loggerInner.info("----already in tingyuan!!!")
        self.you_qing()



if __name__ == '__main__':
    # thisFile = os.path.abspath(__file__)
    # classlists=[]
    # suits=[]
    # processes = []
    # with open(thisFile,"r") as f:
    #     line = f.readline()
    #     if "class" in line and "Tests" in line:
    #         signleClass = re.match(r'class (.*)\(', line).group(1)
    #         suit = unittest.TestLoader().loadTestsFromTestCase(signleClass)
    #         processes.append(Process(target=unittest.TextTestRunner(verbosity=2).run, args=(suit,)))
    #         print signleClass
    # for p in processes:
    #     p.start()
    # print "ok"
    # sleep(5)
    suite = unittest.TestLoader().loadTestsFromTestCase(sigleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)






