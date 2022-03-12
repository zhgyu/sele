#导包
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#获取浏览器驱动对象
driver = webdriver.Chrome()
driver.get("http://192.168.31.83:8080/community/index")
#最大化
driver.maximize_window()
#隐式等待
driver.implicitly_wait(10)
#点击登录链接
driver.find_element_by_link_text("注册").click()
# driver.find_element_by_css_selector("li[class='nav-item ml-3 btn-group-vertical']>a[class='nav-link']").click()
#输入用户名
user = WebDriverWait(driver,10,0.1).until(lambda x:x.find_element_by_css_selector("#username"))
user.send_keys("xiongmao")
#输入密码
driver.find_element_by_css_selector("#password").send_keys("123456")
#输入确认密码
driver.find_element_by_css_selector("#confirm-password").send_keys("123456")
time.sleep(2)
#点击注册按钮
driver.find_element_by_css_selector("button[class='btn btn-info text-white form-control']").click()
time.sleep(2)
#获取错误信息
text=driver.find_element_by_xpath("//form/div[4]/div/div").text
print(text)
driver.quit()