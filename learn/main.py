from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time

def id_get(driver,url):
    driver.get(url)
    #输入用户名admin+密码123456,暂停3秒退出驱动
    # user = driver.find_element_by_id('username')
    # psw = driver.find_element_by_id('password')
    # user = driver.find_element_by_name('username')
    # psw = driver.find_element_by_name('passwordText')
    # user = driver.find_element_by_class_name('text')
    # psw = driver.find_element_by_class_name('password')
    # user = driver.find_element_by_tag_name("input")
    # psw = driver.find_element_by_name('passwordText')
    # user.send_keys("admin")
    # psw.send_keys("123456")
    # driver.find_element_by_link_text("在线帮助").click()
    # driver.find_element_by_partial_link_text("在线").click()
    time.sleep(3)
    driver.quit()
def xpath_get(driver,url):
    driver.get(url)
    userpth = "/html/body/div[@class='container']/div[@class='wrap']" \
              "/section[@class='main']/div[@class='login-pc']/div[@id='pwdLoginDiv']" \
              "/div/form[@id='pwdFromId']/div[@class='form']/div[@class='m-account']" \
              "/div[@class='username item']/input[@id='username']"
    driver.find_element_by_xpath(userpth).send_keys("admin")
    time.sleep(2)
    pswpth = "//input[@id='password']"
    driver.find_element_by_xpath(pswpth).send_keys("123456")
    time.sleep(2)
    loginpth ="//a[@id='login_submit']"
    driver.find_element_by_xpath(loginpth).click()
    time.sleep(16)
    driver.quit()
def css_get(driver,url):
    driver.get(url)
    driver.find_element_by_css_selector('#username').send_keys("admin")
    driver.find_element_by_css_selector("[name='passwordText']").send_keys("1223456")
    helptext=driver.find_element_by_css_selector("a[class='online-help']").text
    print(helptext)
    driver.find_element_by_css_selector('.help>a').click()
    time.sleep(6)
    driver.quit()

def web_relate(driver,url):
    driver.get(url)
    #浏览器最大化    设置固定大小300,200   移动浏览器位置x:320,y:150
    #返回最大化    访问新链接    回退     前进
    driver.maximize_window()
    time.sleep(2)
    driver.set_window_size(300,200)
    time.sleep(2)
    driver.set_window_position(320,150)
    time.sleep(2)
    driver.maximize_window()
    driver.find_element_by_css_selector("#retrievePassId").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()

def mouse_get(driver,url):
    driver.get(url)
    action=ActionChains(driver)
    #右击
    action.context_click(driver.find_element_by_css_selector("#username")).perform()
    psw=driver.find_element_by_css_selector("#password")
    psw.send_keys("123456")
    #双击
    action.double_click(psw).perform()
    #悬停
    login = driver.find_element_by_css_selector("#login_submit")
    action.move_to_element(login).perform()
    #拖拽
    source = driver.find_element_by_css_selector(".source")
    target=driver.find_element_by_css_selector(".target")
    action.drag_and_drop(source,target).perform()

def keyboard_get(driver,url):
    driver.get(url)
    #输入用户名：admin1暂停2秒删除1
    #全选用户名admin暂停2秒
    #复制用户名admin暂停2秒，粘贴到密码框
    user = driver.find_element_by_css_selector("#username")
    user.send_keys("admin1")
    time.sleep(2)
    user.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
    user.send_keys(Keys.CONTROL,"A")
    time.sleep(2)
    user.send_keys(Keys.CONTROL,"C")
    time.sleep(2)
    driver.find_element_by_css_selector("#password").send_keys(Keys.CONTROL,"V")
def wait_two(driver,url):
    #隐式等待
    driver.implicitly_wait(30)#针对所有元素生效，30秒，一般前置必写
    driver.get(url)
    driver.find_element_by_css_selector("#username1").send_keys("admin")
    #显式等待
    usr=WebDriverWait(driver, 10, poll_frequency=0.5).until(lambda x: x.find_element_by_css_selector("#username1"))
    usr.send_keys("admin")

def upload_file(driver,url):
    driver.get(url)
    driver.find_element_by_css_selector("#h5Input1").send_keys(r"C:\Users\y\Desktop\图片1")

def control_get(driver,url):
    driver.implicitly_wait(10)
    driver.get(url)
    #下拉框:定位选项元素，使用click()实现选中
    driver.find_element_by_css_selector("select option[value='saab']").click()
    time.sleep(2)
    #下拉框:使用select类的方法实现选中option
    select = Select(driver.find_element_by_css_selector("select"))
    select.select_by_index(2)
    select.select_by_value("audi")
    select.select_by_visible_text("Volvo")

def three_input(driver,url):
    driver.get(url)
    # driver.find_element_by_css_selector("#button1").click()
    # driver.find_element_by_css_selector("#button2").click()
    driver.find_element_by_css_selector("#button3").click()
    time.sleep(2)
    alt = driver.switch_to_alert()
    print(alt.text)
    alt.accept()
    alt.dismiss()
    driver.find_element_by_css_selector("#username").send_keys("admin")

def scroll_get(driver,url):
    driver.get(url)
    time.sleep(2)
    js = "window.scrollTo(0,10000)"
    driver.execute_script(js)

def frame_get(driver,url):
    driver.get(url)
    """主页面操作"""
    driver.switch_to.frame('frame_id_or_name1')
    """frame——id_name1页面操作"""
    driver.switch_to.default_content()
    driver.switch_to.frame('frame_id_or_name2')
    """frame_id_name2页面操作"""
    driver.switch_to.default_content()
def window_handle_get(driver,url):
    driver.get(url)
    current_handle = driver.current_window_handle
    #跳转页面
    driver.find_element_by_css_selector(".online-help").click()
    driver.implicitly_wait(5)
    window_handle = driver.window_handles
    print("当前窗口",current_handle)
    print("所有窗口",window_handle)
    for h in window_handle:
        if h!=current_handle:#判断不为默认页面就跳转窗口
            driver.switch_to.window(h)
            print("切换")
    next_window = driver.current_window_handle
    print("当前窗口",next_window)
    print(driver.find_element_by_css_selector("h6").text)

def screen_get(driver,url):
    driver.get(url)
    driver.find_element_by_css_selector("#username").send_keys("admin")
    imgpath=r"C:\Users\y\Desktop\screen.png"
    driver.get_screenshot_as_file(imgpath)
    # driver.get_screenshot_as_png()
    # driver.get_screenshot_as_base64()

def cookie_get(driver,url):
    url = "https://www.baidu.com"
    driver.get(url)
    #使用cookie登录百度，获取cookie，达到登录目的执行登录后的操作
    driver.add_cookie({'name':'BDUSS','value':'pLZ2RWeEJHaFFRTXQ4SWo2WXl1YzdJSVlzTjRSTjN-dS1tTTZFMDN0VXcwYWhoRVFBQUFBJCQAAAAAAAAAAAEAAAA0B8Iy0KHR9Ljn0rvWsdTaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBEgWEwRIFhTk'})
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_css_selector("#kw").send_keys("搜索")


if __name__ == '__main__':
    driver= webdriver.Chrome()
    url = "https://ids.cqupt.edu.cn/authserver/login?service=http%3A%2F%2Fehall.cqupt.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.cqupt.edu.cn%2Fnew%2Findex.html"
    url1=r"C:\Users\y\Desktop\a.html"
    url2=r"E:\python_test\sele\alert.html"
    url3="https://www.bilibili.com/video/BV1QJ41137gj?p=66&spm_id_from=pageDriver"
    cookie_get(driver,url)







