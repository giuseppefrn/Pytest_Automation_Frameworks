from pytest import mark

@mark.entertainment
def test_entertainment_functions_as_expected():
    assert True

@mark.ui
def test_can_navigate_to_entertainment(chrome_browser):
    chrome_browser.get('https://www.caranddriver.com/')
    assert True