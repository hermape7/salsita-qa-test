from selenium.webdriver.common.by import By


class ListsPageLocators:
    SPAN_SCORE_LIST = (By.CSS_SELECTOR, 'span.score')
    QUOTES_HEADLINE_LIST = (By.CSS_SELECTOR, 'body > ul > li > strong')

    QUOTES_LIST = (By.CSS_SELECTOR, 'body > ul > li > ul')
    BODY = (By.CSS_SELECTOR, 'body')

    @classmethod
    def get_quote_list(cls, index):
        return By.XPATH, '//ul/li[{}]/ul/li'.format(index + 1)
        # return {
        #     index: '//ul/li[{}]/ul/li'.format(index)
        # }.get(index)
