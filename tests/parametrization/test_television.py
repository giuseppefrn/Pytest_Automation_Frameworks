
from pytest import mark

# Most basic example (not very useful)
# @mark.skip
# @mark.parametrize('tv_model', [
#     ('Samsung'),
#     ('Sony'),
#     ('Xiaomi')
# ])


def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on")

@mark.skip
def test_browser_can_navigate_to_giuseppefrn(browser):
    browser.get("https://github.com/giuseppefrn")
