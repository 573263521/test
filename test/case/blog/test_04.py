#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       # cls.driver=webdriver.PhantomJS()
        cls.driver=webdriver.Firefox()
        cls.driver.get("https://www.baidu.com")
        time.sleep(2)
        a=cls.driver.find_element_by_link_text('设置')
        b=cls.driver
        ActionChains(b).move_to_element(a).perform()
        time.sleep(3)
        cls.driver.find_element_by_link_text('搜索设置').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        a=self.driver.find_element_by_xpath("//option[@value='20']").text
        b='每页显示20条'
        self.assertEqual(a,b)
        print(a)
    def test02(self):
        a=self.driver.find_element_by_xpath("//label[@for='s1_1']").text
        b='显示'
        self.assertEqual(a,b)
        print(a)
    def test03(self):
        a=self.driver.find_element_by_xpath("//option[@value='2']").text
        b='关闭'
        self.assertEqual(a,b)
        print(a)
if __name__ =="__main__":
    unittest.main
