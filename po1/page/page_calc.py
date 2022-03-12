from po1.base.base import Base
from selenium.webdriver.common.by import By
from po1 import page
class PageCalc(Base):
    #点击数字方法
    def page_click_num(self,num):
        for n in str(num):
            #组装格式：拆开单个按钮的定位方式
            loc = (By.CSS_SELECTOR,"#simple{}".format(n))
            self.base_click(loc)
    #点击加号
    def page_click_add(self):
        self.base_click(page.cal_add)
    #点击等号
    def page_click_equal(self):
        self.base_click(page.cal_equal)
    #获取结果方法
    def page_get_result(self):
        return self.base_get_input_value(page.cal_reault)
    #点击清屏
    def page_clear(self):
        self.base_click(page.cal_clear)
    #获取截图
    def page_get_screen_shot(self,pth=""):
        self.base_get_screen_shot(pth)
    #加法测试
    def page_add_calc(self,a,b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_equal()