import unittest

import pytest

import constants
from pages.home_page import HomePage


@pytest.mark.usefixtures('get_driver')
class TestQaEngFlow(unittest.TestCase):

    def setUp(self):
        self.driver.get(constants.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_qa_eng_flow(self):
        # init HomePage page to click enter button
        homepage = HomePage(self.driver)
        code_page = homepage.click_enter_btn()

        # Find and fill secret value to input
        val = code_page.get_hidden_input_value()
        code_page.fill_code_input()
        print('Entered {} value to input.'.format(val))

        # verify, that checkbox is selected
        code_page.is_robot_checkbox_selected()

        # proceed to lists page
        lists_page = code_page.click_submit_btn()

        # Check quotes headlines and each quote in particular list
        assert lists_page.check_quotes() is True

        # Checks number of quotes
        awesome_list_len = len(lists_page.get_awesome_quotes_list())
        assert awesome_list_len == 5, 'There is a bad value ({}) of quotes in awesome list. It should be 5'.format(
            awesome_list_len)
        print('Number of total quotes in awesome quote list is {}'.format(awesome_list_len))

        famous_list_len = len(lists_page.get_famous_quotes_list())
        assert famous_list_len == 5, 'There is a bad value ({}) of quotes in famous list. It should be 5'.format(
            famous_list_len)
        print('Number of total quotes in famous quote list is {}'.format(famous_list_len))

        # get total score from quotes
        total_score_from_quotes = lists_page.get_score_from_all_quotes()
        print('Total score from quotes is {}'.format(total_score_from_quotes))

        # get total score
        total_score = lists_page.get_total_score()
        print('Total score is {}'.format(total_score))
        assert total_score_from_quotes == total_score, 'Score in all quotes ({}) mismatch from total score ({})'.format(
            total_score_from_quotes, total_score)
