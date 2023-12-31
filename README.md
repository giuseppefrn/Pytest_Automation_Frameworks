# PYTEST AUTOMATION FRAMEWORKS
Notes on how to use Pytest and explore its functionalities.

Credits to [Elegant Automation Frameworks with Python and Pytest](https://www.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/). To know more check the original course at the previous link, this repo is only intended as personal notes. 

## Details
This repository covers the Pytest Framework. For this reason, you may like to check out the [Pytest documentation](https://docs.pytest.org/en/latest/).

## Usage
There are different conftest files, so if you want to run a test be sure to be in the correct parent directory and not in the root.

## Some useful notes
- General
  - To customize the test search modify the `pytest.ini` file
  - Use `-s` to show your standard output
- Marks
  - To mark tests import `mark` from `pytest` and mark them using the decorator `@mark.yourmark`
  - To run only marked test run `pytest -m yourmark` or a combination i.e. `pytest -m "yourmark or yourothermark"`
  - Add your marks in the `pytest.ini` file and check them running `pytest --markers`
- Fixture
  - Generate a `conftest.py` file for more detail check an example [here](/tests/sportscar/conftest.py)
- Test reporting
  - Generate a results.xml by using the argument `junitxml`, i.e. `pytest --junitxml="results.xml"`
- Parser options
  - Check an example in [conftest.py](/tests/configuration/conftest.py)
- [Skips](https://docs.pytest.org/en/latest/how-to/skipping.html) and xfail
  - used in [test_engine.py](tests/configuration/test_configuration.py)
- Parallelization
  - install `pytest-xdist` and use the argument `-n` followed by the number of threads you want to use i.e. `-n4` 