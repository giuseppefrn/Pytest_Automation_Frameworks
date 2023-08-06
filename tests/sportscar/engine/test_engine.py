from pytest import mark

@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

@mark.ui
def test_can_navigate_to_engine(chrome_browser):
    chrome_browser.get('https://www.howacarworks.com/')
    assert True

@mark.appconf
def test_environment_is_qa(app_config):
    assert app_config.base_url == 'https://myqa-env.com'
    assert app_config.app_port == 80
