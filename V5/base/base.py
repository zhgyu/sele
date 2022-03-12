from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium import webdriver
from V5.tools.get_log import get_logging
from V5.tools.get_logger import GetLogger
# log = get_logging()
logger = GetLogger().get_logger()
class Base:
    #初始化获取driver
    def __init__(self,driver):
        self.driver = driver
        # log.info("初始化driver{}".format(driver))
        logger.info("初始化driver{}".format(driver))
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.get("http://192.168.31.83:8080/community/index")
        # self.driver.implicitly_wait(3)
    #查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        """
        :param loc: 元素的配置信息，格式为元组，如register_link=(By.LINK_TEXT,"注册")
        :param timeout: 默认超时时间为30，可通过传入参数进行修改
        :param poll: 默认访问频率为0.5秒
        :return: 查找到的元素
        """
        # log.info("查找元素{}".format(loc))
        logger.info("查找元素{}".format(loc))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    def base_if_exist(self,loc):
        try:#找到元素返回TRUE
            self.base_find_element(loc)
            return True
        except:
            return False
    #点击
    def base_click(self,loc):
        # log.info("元素{}执行点击".format(loc))
        logger.info("元素{}执行点击".format(loc))
        self.base_find_element(loc).click()
    #输入
    def base_input(self,loc,value):
        element=self.base_find_element(loc)
        element.clear()
        # log.info("元素{}清空".format(loc))
        logger.info("元素{}清空".format(loc))
        element.send_keys(value)
        # log.info("向元素{}输入{}".format(loc,value))
        logger.info("向元素{}输入{}".format(loc,value))
    #获取文本
    def base_get_text(self,loc):
        # log.info("获取元素{}文本".format(loc))
        logger.info("获取元素{}文本".format(loc))
        return self.base_find_element(loc).text
    #截图
    def base_get_screen_shot(self,pth):
        self.driver.get_screenshot_as_file("../{}_{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S"),pth))