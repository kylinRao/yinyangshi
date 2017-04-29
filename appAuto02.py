import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'kindle fire HD'
        desired_caps['appPackage'] = 'com.netease.onmyoji.huawei'
        desired_caps['appActivity'] = 'com.netease.onmyoji.Launcher'
        
        
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        


        

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        #el = self.driver.find_element_by_name("Add Contact")
        sleep(5)
        self.driver.tap((92,76))




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
