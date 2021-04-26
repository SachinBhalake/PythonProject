# import statements
from selenium import webdriver
import pytest

# setup method
@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup(request):

    # browser config
    try:

        if request.param == "chrome":
            driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

        if request.param == "firefox":
            driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

        if request.param == "edge":
            driver = webdriver.Edge(executable_path="Drivers/msedgedriver.exe")

        driver.maximize_window()
        request.instance.driver = driver

        # closing browser at the end
        yield driver
        driver.close()

    except Exception:
        assert False

# end of the setup method