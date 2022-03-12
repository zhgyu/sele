from selenium.webdriver.common.by import By
num="65489123"
for i in num:
    calc_num = (By.CSS_SELECTOR,"simple{}".format(i))
    print(calc_num)