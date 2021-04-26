# import statements
from selenium.common.exceptions import *
from selenium import webdriver
import time
import random
from selenium.webdriver.support.ui import Select
import pytest
from datetime import datetime
from read_csv import getCSVData
from setup import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# class definition using fixture setup
@pytest.mark.usefixtures("setup")
class Test_practice:

    @pytest.mark.simpletest
    def test_simple(self):

        try:
            self.driver.get("https://www.google.com/")

            time.sleep(2)

            input_url = "https://www.google.com/"

            current_url = self.driver.current_url

            assert (input_url==current_url)

        except Exception:

            assert False
