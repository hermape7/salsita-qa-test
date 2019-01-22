from locators.code_page_locators import CodePageLocators
from pages.base_page import BasePage
from pages.lists_page import ListsPage


class CodePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_hidden_input_value(self):
        return self.get_element_value(CodePageLocators.SECRET_INPUT)

    def click_submit_btn(self):
        self.click_element(CodePageLocators.SUBMIT_BTN)
        return ListsPage(self.driver)

    def fill_code_input(self):
        return self.fill_input_field(CodePageLocators.CODE_INPUT, self.get_hidden_input_value())

    def is_robot_checkbox_selected(self):
        """
        Check, if Robot checkbox is selected. If not, checkbox will be checked.

        :return: Boolean
        """
        if not self.get_element(CodePageLocators.CHECKBOX_ROBOT).is_selected():
            print('Checkbox is not selected. Checking it.')
            self.click_element(CodePageLocators.CHECKBOX_ROBOT)

        assert self.get_element(CodePageLocators.CHECKBOX_ROBOT).is_selected() is True, 'Checkbox is not selected.'
