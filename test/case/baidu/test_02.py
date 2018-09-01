#coding:utf-8
from selenium import webdriver
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.PhantomJS()
        #cls.driver = webdriver.Firefox()
        cls.driver.get("https://mail.qq.com")
        time.sleep(2)
        cls.driver.switch_to_frame("login_frame")
        cls.driver.find_element_by_id("u").send_keys("573263521")
        time.sleep(3)
        cls.driver.find_element_by_id('p').send_keys("wjxqy666..")
        cls.driver.find_element_by_id("login_button").click()
        cls.driver.switch_to_default_content()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        a =self.driver.find_element_by_id("composebtn").text
        b='写信'
        self.assertEqual(a,b)
        print(a)
    def test02(self):
        a=self.driver.find_element_by_xpath("//*[@id='useralias']").text
        b='王甲希'
        print(a)
    def test03(self):
        a=self.driver.find_element_by_xpath("//div[@class='left']/span[1]").text
        b='573263521@qq.com'
        print(a)
if __name__ == "__main__":
    unittest.main