import pytest
from selenium import webdriver


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser not supported")

    driver.maximize_window()
    yield driver
    driver.quit()
