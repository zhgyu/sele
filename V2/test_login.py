#导包
import unittest
from selenium import webdriver
import time
#新建测试类并继承
class TestLogin(unittest.TestCase):
    #setup
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.31.83:8080/community/index")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    #teardown
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    #新建测试函数
    def test_login_exmail_not_null(self):
        self.driver.find_element_by_link_text("注册").click()
        self.driver.find_element_by_css_selector("#username").send_keys("xiongmao")
        self.driver.find_element_by_css_selector("#password").send_keys("123456")
        self.driver.find_element_by_css_selector("#confirm-password").send_keys("123456")
        self.driver.find_element_by_css_selector("button[class='btn btn-info text-white form-control']").click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath("//form/div[4]/div/div").text
        # print(result)
        try:
            self.assertEqual(result,"邮箱不能为空！")
            print("test_login_exmail_not_null:",result)
        except AssertionError:
            self.driver.get_screenshot_as_file("./{}_test_login_exmail_not_null_fail.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))


    def test_login_username_unique(self):
        self.driver.find_element_by_link_text("注册").click()
        self.driver.find_element_by_css_selector("#username").send_keys("xiongmao")
        self.driver.find_element_by_css_selector("#password").send_keys("123456")
        self.driver.find_element_by_css_selector("#confirm-password").send_keys("123456")
        self.driver.find_element_by_css_selector("#email").send_keys("busly9@163.com")
        self.driver.find_element_by_css_selector("button[class='btn btn-info text-white form-control']").click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath("//form/div[1]/div/div").text
        try:
            self.assertEqual(result,"该用户名已存在")
            print("test_login_username_unique:",result)
        except AssertionError:
            self.driver.get_screenshot_as_file("./{}_test_login_username_unique_fail.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))


