import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser', dest='browser', default='chrome', help='Choose browser (chrome or ff). Default is chrome'
    )


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture
def get_driver(request):
    request.cls.driver = webdriver.Chrome()
    # if browser == 'chrome':
    #     request.cls.driver = webdriver.Chrome()
    # elif browser == 'firefox' or browser == 'ff':
    #     request.cls.driver = webdriver.Firefox()
    # else:
    #     raise NotImplementedError('Not implemented for {} browser'.format(browser))
