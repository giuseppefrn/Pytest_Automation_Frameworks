# Only test in the same directory or deeper can access to it and NO need to import it

from pytest import fixture
from selenium import webdriver

from config import Config

def pytest_addoption(parser): #no need to import or provide parser
    parser.addoption("--env", action="store", help="Env to run tests against")

# scope of the fixture can be session (i.e. one browser per session), function (one browser per function/test), class, module and package
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env") #request hold all the arguments option

@fixture(scope="session")
def app_config(env): # a fixture can use a fixture
    cfg = Config(env) 
    return cfg
