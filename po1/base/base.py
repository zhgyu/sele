#初始化
#查找元素
#点击
#获取input的value值
#获取截图
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
class Base():
    def __init__(self,driver):
        self.driver = driver
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def base_click(self,loc):
        self.base_find_element(loc).click()

    def base_get_input_value(self,loc):
        return self.base_find_element(loc).get_attribute("value")

    def base_get_screen_shot(self,pth=""):
        self.driver.get_screenshot_as_file("../{}_{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S"),pth))