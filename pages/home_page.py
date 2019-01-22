from locators.home_page_locators import HomePageLocators
from pages.code_page import CodePage
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_enter_btn(self):
        self.click_element(HomePageLocators.ENTER_BTN)
        return CodePage(self.driver)
