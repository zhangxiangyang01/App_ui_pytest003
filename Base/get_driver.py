from appium import webdriver
# from selenium.webdriver import TouchActions

def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    desired_caps['appPackage'] = 'aolei.buddha'
    desired_caps['appActivity'] = '.login.activity.LoginActivity'

    desired_caps['autoGrantPermissions'] = 'true'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



