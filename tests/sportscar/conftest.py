# Only test in the same directory or deeper can access to it and NO need to import it

from pytest import fixture
from selenium import webdriver


# scope of the fixture can be session (i.e. one browser per session), function (one browser per function/test) and module
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser