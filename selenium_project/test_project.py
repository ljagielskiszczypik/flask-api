import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from locators import Billing_locators
from Test_methods import test_change_billing
from conftest import Test_Base
@pytest.mark.usefixtures('test_setup')
class Test_projekt(Test_Base):
   def test_continue(self,test_setup):
       Billing=test_change_billing(self.driver)
       Billing.sing_up()
       Billing.changing_billing()
