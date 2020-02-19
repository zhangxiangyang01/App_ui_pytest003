import os, sys
sys.path.append(os.getcwd())

from Page.page_in import PageIn

import pytest

from Base.get_driver import get_driver
from Page.page_login import PageLogin

class TestLogin():

    # 初始化方法
    def setup_class(self):

        # self.driver = get_driver()

        # ------ 实例化 PageLogin
        self.login = PageLogin(get_driver())

        # ------ PageIn
        # self.login = PageIn.page_get_login(get_driver())
    # 结束方法
    def teardown_class(self):

        # 关闭驱动对象

        # self.driver.quit()
        self.login.driver.quit()

    def test_login(self,username="18339052997@163.com", pwd="123456"):

        # self.login.page_click_wo()

        # self.login.page_click_wei()
        #
        # self.login.page_click_mail()

        self.login.page_input_username(username)

        self.login.page_input_password(pwd)

        self.login.page_click_login_btn()

if __name__ == '__main__':
    pytest.main("-s test_login.py")

