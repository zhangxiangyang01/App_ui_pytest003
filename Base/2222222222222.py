from time import sleep

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

desired_caps['appPackage'] = 'aolei.buddha'
desired_caps['appActivity'] = '.login.activity.LoginActivity'

desired_caps['autoGrantPermissions'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_xpath("//*[contains(@text,'登录') and contains(@resource-id,'login_commit')]").click()
# sleep(1)
print(driver.find_element_by_xpath("//*[contains(@class='android.widget.LinearLayout.Toast')]").text)

