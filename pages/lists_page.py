import constants
from locators.lists_page_locators import ListsPageLocators
from pages.base_page import BasePage


class ListsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.awesome_quotes_list = None
        self.famous_quote_list = None

    def get_score_from_all_quotes(self):
        total_score = 0
        for score in self.get_elements_list(ListsPageLocators.SPAN_SCORE_LIST):
            total_score += int(score.text)
        return int(total_score)

    def get_total_score(self):
        text = self.get_element_text(ListsPageLocators.BODY)
        ret_val = None
        for string in text.split():
            if string.isdigit():
                ret_val = int(string)
        return ret_val

    def check_quotes(self):
        are_quotes_valid = False
        for i, headline in enumerate(self.get_elements_list(ListsPageLocators.QUOTES_HEADLINE_LIST)):
            headline_text = headline.text.lower().strip()
            if headline_text in constants.HEADLINE_LIST:
                print('Headline ({}) is in list {}'.format(headline_text, constants.HEADLINE_LIST))
                if headline_text == constants.AWESOME_QUOTES_HEADLINE:
                    are_quotes_valid = self._check_awesome_quotes(i)
                elif headline_text == constants.FAMOUS_QUOTES_HEADLINE:
                    are_quotes_valid = self._check_famous_quotes(i)
            else:
                print('Headline ({}) is NOT in list {}'.format(headline_text, constants.HEADLINE_LIST))
                are_quotes_valid = False
        return are_quotes_valid

    def _check_awesome_quotes(self, index):
        self.awesome_quotes_list = self.get_elements_list(ListsPageLocators.get_quote_list(index))
        for quote in self.awesome_quotes_list:
            assert quote.is_displayed() is True, 'Quote "{}" is not displayed.'.format(quote)
            assert quote.text[
                   :-4].strip() in constants.AWESOME_QUOTES_LIST, 'Quote "{}" is not in awesome list.'.format(
                quote.text[:-4].strip())
        return True

    def _check_famous_quotes(self, index):
        self.famous_quote_list = self.get_elements_list(ListsPageLocators.get_quote_list(index))
        for quote in self.famous_quote_list:
            assert quote.is_displayed() is True, 'Quote "{}" is not displayed.'.format(quote)
            assert quote.text[:-4].strip() in constants.FAMOUS_QUOTES_LIST, 'Quote "{}" is not famous in list.'.format(
                quote.text[:-4].strip())
        return True

    def get_awesome_quotes_list(self):
        return self.awesome_quotes_list

    def get_famous_quotes_list(self):
        return self.famous_quote_list
