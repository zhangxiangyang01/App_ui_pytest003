from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestDemo():

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '192.168.56.101:1111'
        desired_caps['appPackage'] = 'aolei.buddha'
        desired_caps['appActivity'] = '.login.activity.LoginActivity'
        desired_caps['autoGrantPermissions'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        # if len(self.driver.find_elements_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()

        # WebDriverWait(self.driver, 10, 0.5).until(lambda x: self.driver.find_elements_by_id("image_cancel") >=1)
        WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.visibility_of_element_located((By.ID,"image_cancel")))
        self.driver.find_element_by_id("image_cancel").click()

        TouchAction(self.driver).long_press().move_to().wait(1000).release().perform()
        save = self.driver.find_element_by_xpath("//*[contains(@text,'qifu')]")
        more = self.driver.find_element_by_xpath("//*[contains(@text,'t0utiao')]")
        self.driver.swipe(save.location.get("x"),save.location.get("y"),more.location.get("x"),more.location.get("y"),duration=3000)
        print(self.driver.get_window_size())

    def test_gsm(self):
        self.driver.send_sms("18339052997","hello,你好")
        self.driver.make_gsm_call("18339052997",GsmCallActions.CALL)

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        # self.driver.get_performance_data('aolei.buddha','batteryinto',5)
        for i in self.driver.get_performance_data():
            try:
                print(self.driver.get_performance_data('aolei.buddha', i, 5))
            except:
                pass
    def test_002(self):
        pass
    
    def test_003(self):
        pass
    
    def test_004(self):
        pass

    def test_005(self):
        pass
    
    def test_xpath(self):
    # "//*[contains(@text,'登录') and contains(@resurse-id,'login')]"
        self.driver.find_element_by_xpath("//*[contains(@text,'登录') and contains(@resource-id,'login_commit')]").click()
        self.driver.find_element_by_accessibility_id("sourch")

    def test_toast(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'登录') and contains(@resource-id,'login_commit')]").click()
        print(self.driver.find_element_by_xpath("//*[contains(@class='android.widget.LinearLayout.Toast')]").text)

    def tearDown(self):
        self.driver.quit()
