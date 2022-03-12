from selenium import webdriver
from po1 import page
class GetDriver:
    driver = None
    @classmethod
    def get_driver(cls):
        if(cls.driver is None):
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
            cls.driver.implicitly_wait(10)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            #注意!!!!!!一定要还原   驱动对象关闭但session不会立即改变，内存地址依然占用
            cls.driver = None