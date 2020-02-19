# from selenium.webdriver.common.by import By
from Base.base import Base

import Page

class PageLogin(Base):

    # #点击我的
    # def page_click_wo(self):
    #     self.base_click(loc_wo_btn)
    # 点击未登录
    # def page_click_wei(self):
    #     self.base_click(loc_wei_btn)
    # # 点击网易邮箱登陆
    # # 点击登陆
    # def page_click_mail(self):
    #     self.base_click(loc_mail_btn)

    # 输入用户名
    def page_input_username(self, text):
        self.base_input(Page.loc_name, text)

    # 输入密码
    def page_input_password(self, text):
        self.base_input(Page.loc_pwd, text)

    # 点击登陆
    def page_click_login_btn(self):
        self.base_click(Page.loc_deng_btn)


