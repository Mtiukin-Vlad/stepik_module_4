import pytest

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="uk",
                     help="Choose language: ru, hu")

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")
    yield language