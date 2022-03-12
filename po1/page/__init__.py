"""
服务器配置数据
"""
url = "http://cal.apple886.com/"
"""
页面配置数据
"""
from selenium.webdriver.common.by import By
cal_add = (By.CSS_SELECTOR,"#simpleAdd")
cal_equal = (By.CSS_SELECTOR,"#simpleEqual")
cal_reault = (By.CSS_SELECTOR,"#resultIpt")
cal_clear = (By.CSS_SELECTOR,"#simpleClearAllBtn")