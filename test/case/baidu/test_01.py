#coding:utf-8
import unittest,time
from selenium import webdriver
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.PhantomJS()
        cls.driver=webdriver.Firefox()
        cls.driver.get("https://mail.163.com")
        time.sleep(2)
        cls.driver.switch_to_frame('x-URS-iframe')
        print('start')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def login(self, username, password):
        self.driver.find_element_by_xpath("//*[@name='email']").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()
        self.driver.switch_to_default_content()
        time.sleep(2)
    def test01(self):
        self.login('wjx573263521', 'wjxqy666..')
        a = self.driver.find_element_by_xpath("//span[@class='js-component-component gWel-greet-trueName']").text
        print(a)
        self.assertEqual(a, '王甲希，')
    def test02(self):
        b = self.driver.find_element_by_xpath("//span[@id='spnUid']").text
        print(b)
        self.assertEqual(b, 'wjx573263521@163.com')
        time.sleep(2)
    def test03(self):
        self.driver.find_element_by_xpath("//*[@id='_mail_component_69_69']/span[2]").click()
        c = self.driver.find_element_by_xpath("//*[@class='nui-toolbar-item']/div/span[2]").text
        print(c)
        self.assertEqual(c, '发送')
if __name__ == '__main__':
    unittest.main
