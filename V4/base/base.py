from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium import webdriver
class Base:
    #初始化获取driver
    def __init__(self):
        # self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.31.83:8080/community/index")
        self.driver.implicitly_wait(3)
    #查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #点击
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #输入
    def base_input(self,loc,value):
        element=self.base_find_element(loc)
        element.clear()
        element.send_keys(value)
    #获取文本
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    #截图
    def base_get_screen_shot(self,pth):
        self.driver.get_screenshot_as_file("../{}_{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S"),pth))