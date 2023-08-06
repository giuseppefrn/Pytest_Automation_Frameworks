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

@mark.skip(reason="Not dev environment")
@mark.appconf
def test_dev_environment_port(app_config):
    assert app_config.app_port == 8080

@mark.xfail(reason="Env was not dev")
@mark.appconf
def test_dev_environment_url(app_config):
    assert app_config.base_url == 'https://mydev-env.com'
