import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
class BaseTest:
   @pytest.fixture()
   def test_setup(self):
       self.driver = webdriver.Chrome(service=service, options=options)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)
       yield
       self.driver.quit()