import pytest
from selenium import webdriver


# to execute from the command line terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # setting up the chrome drivers
        driver = webdriver.Chrome(executable_path="//Users/subathra/Documents/Selenium/chromedriver")
    elif browser_name == "firefox":
        # setting up the firefox drivers
        driver = webdriver.Firefox(executable_path="/Users/subathra/Documents/Selenium/geckodriver")

    # Initializing the url
    driver.get("https://clarity.dexcom.com/")

    # Maximizing the window to make sure the elements are visible
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()
