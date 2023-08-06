import json

from pytest import fixture
from selenium import webdriver

data_path = "test_data.json"

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=[webdriver.Chrome, webdriver.Edge]) #every test that use this fixture will run N times depending the params
def browser(request):
    driver = request.param #return the parameter 
    drvr = driver() #calling the class and instantiate it 
    yield drvr

    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data