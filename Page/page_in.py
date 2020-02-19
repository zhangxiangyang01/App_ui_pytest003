from Base.get_driver import get_driver
from Page.page_address import PageAddress
from Page.page_login import PageLogin
from Page.page_setting import PageSetting

driver = get_driver()

class PageIn():


    def page_get_address(self):
        return PageAddress(driver)

    def page_get_login(self):
        return PageLogin(driver)

    def page_get_setting(self):
        return PageSetting(driver)