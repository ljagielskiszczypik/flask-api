import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
class Test_Base:
   @pytest.fixture()
   def test_setup(self):
       self.driver = webdriver.Chrome(service=service, options=options)
       self.driver.get('http://seleniumdemo.com/')
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)
       yield
       self.driver.quit()