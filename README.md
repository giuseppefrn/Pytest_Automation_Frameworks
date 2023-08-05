# PYTEST AUTOMATION FRAMEWORKS
Notes on how to use Pytest and explore its functionalities.

Credits to [Elegant Automation Frameworks with Python and Pytest](https://www.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/). To know more check the original course at the previous link, this repo is only intended as personal notes. 

## Details
This repository covers the Pytest Framework. For this reason, you may like to check out the [Pytest documentation](https://docs.pytest.org/en/latest/).

## Some useful notes
To customize the test search modify the `pytest.ini` file
- To mark tests import `mark` from `pytest` and mark them using the decorator `@mark.yourmark`
- To run only marked test run `pytest -m yourmark` or a combination i.e. `pytest -m "yourmark or yourothermark"`
- Add your marks in the `pytest.ini` file and check them running `pytest --markers`