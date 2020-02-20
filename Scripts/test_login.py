import os, sys
sys.path.append(os.getcwd())
import pytest
import allure
from Base.read_login_yaml import get_yaml
from Page.page_in import PageIn
from Base.get_driver import get_driver
from Page.page_login import PageLogin

def get_data():
    arrs = []
    for i in get_yaml().values():
        arrs.append((i.get("username"), i.get("pwd"), i.get("expect_toast")))
    return arrs

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

    # @pytest.mark.parametrize("username,pwd",[("18339052997@163.com", "123456"),("2222222@163.com","222222")])

    @allure.step("登录测试")
    # @pytest.allure.serverity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username,pwd,expect_toast", get_data())
    def test_login(self, username, pwd, expect_toast):

    # def test_login(self,username="18339052997@163.com", pwd="123456"):

        # self.login.page_click_wo()

        # self.login.page_click_wei()
        #
        # self.login.page_click_mail()
        allure.attach("描述：","输入用户名")
        self.login.page_input_username(username)

        allure.attach("描述：", "输入密码")
        self.login.page_input_password(pwd)

        allure.attach("描述：", "提示语")
        print("预期结果为：", expect_toast)

        self.login.page_click_login_btn()

    # @pytest.allure.serverity(pytest.allure.severity_level.NORMAL)
    # def test_002(self):
    #     print("严重级别")



if __name__ == '__main__':
    pytest.main("-s test_login.py")

