import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

class ManageAlertTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://www.cookbook.seleniumacademy.com/Alerts.html")

    @classmethod
    def tearDownClass(cls):
        print("This will run only once after the tearDown method for the last test")

    def setUp(self):
        print("test")

    def test_alert_box(self):
        self.driver.find_element_by_id("simple").click()
        try:
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            time.sleep(3)
            print("alert box - ",alert_message)
            alert.accept()
        except NoAlertPresentException :
            print ("Test case failed")

    def test_confirm_alert(self):
        self.driver.find_element_by_id("confirm").click()

        try:
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            time.sleep(3)
            print("confirm box - ",alert_message)
            alert.dismiss()
            time.sleep(3)
        except NoAlertPresentException :
            print ("Test case failed")

    def test_promt_alert(self):
        self.driver.find_element_by_id("prompt").click()

        try:
            alert = self.driver.switch_to.alert
            alert_message = alert.text
            time.sleep(3)
            print("prompt box - ",alert_message)
            alert.send_keys("Sachin")
            time.sleep(4)
            alert.accept()
        except NoAlertPresentException :
            print ("Test case failed")


if __name__ == '__main__':
    unittest.main(verbosity=2)
