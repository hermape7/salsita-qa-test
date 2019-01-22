from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = 5
        self.wait = WebDriverWait(self.driver, self.delay)
        self.ec = expected_conditions

    def get_element(self, locator):
        """
        Returns element located by given locator.

        :param locator: tuple
        :return: WebElement
        """
        try:
            elem = self.driver.find_element(*locator)
        except NoSuchElementException:
            raise NoSuchElementException('Element with locator [{}] is not found'.format(locator))
        return elem

    def get_elements_list(self, locator):
        """
        Return list of elements located by given locator.

        :param locator: tuple
        :return: WebElement
        """
        try:
            elem_list = self.driver.find_elements(*locator)
        except NoSuchElementException:
            raise NoSuchElementException('Element with locator [{}] is not found'.format(locator))
        return elem_list

    def click_element(self, locator):
        if self._is_element_clickable(locator):
            self.get_element(locator).click()
        else:
            print('Element with locator [{}] is not clickable.'.format(locator))

    def get_element_text(self, locator):
        """
        Returns element text

        :param locator: tuple
        :return: String
        """
        return self.get_element(locator).text

    def get_element_value(self, locator):
        """
        Returns value with get_attribute('value')

        :param locator: tuple
        :return: String
        """
        return self.get_element(locator).get_attribute('value')

    def fill_input_field(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def _is_element_clickable(self, locator):
        """
        Click on element with expected condition syntax. Returns true if it is possible to click on the element.

        :param locator: tuple
        :return: Boolean
        """
        return self.wait.until(lambda x: self.ec.element_to_be_clickable(self.get_element(locator)))

    def is_element_displayed(self, locator, delay=5):
        """
        Click on element with expected condition syntax. Returns true if element is displayed.
        Possible to change delay for waiting to display the element. Default is 5s.

        :param locator: tuple
        :param delay: int
        :return: Boolean
        """
        return WebDriverWait(self.driver, delay).until(
            lambda x: self.get_element(locator).is_displayed())
