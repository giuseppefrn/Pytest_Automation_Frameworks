# Only test in the same directory or deeper can access to it and NO need to import it
from pytest import fixture

from config import Config

def pytest_addoption(parser): #no need to import or provide parser
    parser.addoption("--env", action="store", help="Env to run tests against")

@fixture(scope="session")
def env(request):
    return request.config.getoption("--env") #request hold all the arguments option

@fixture(scope="session")
def app_config(env): # a fixture can use a fixture
    cfg = Config(env) 
    return cfg
