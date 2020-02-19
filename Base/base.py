from selenium.webdriver.support.wait import WebDriverWait

class Base():
    """
    1.打开应用
    2.输入用户名
    3.输入密码
    4.点击登陆
    """
    
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=30, poll_frequency=poll).until(lambda x: x.find_element(*loc))
    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()
    # 输入方法
    def base_input(self,loc,text):
        el = self.base_find(loc)
        el.clear()
        el.send_keys(text)