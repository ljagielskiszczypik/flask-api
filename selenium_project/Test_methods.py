from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service()
options = webdriver.ChromeOptions()
from selenium.webdriver.support.select import Select
from locators import Billing_locators
import random
import logging
class test_change_billing:
   def __init__(self,driver):
       self.email = str(random.randint(1, 10000)) + 'exlares@gmail.com'
       self.password = str(random.randint(1, 10000)) + 'Xilla122@@'
       self.driver = driver
       self.logger = logging.getLogger(__name__)



   def sing_up(self):
       self.driver.get('http://seleniumdemo.com/')
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_myAccount).click()
       self.logger.info('setting {email} as email and {password} as password'.format(email=self.email, password=self.password))
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_email).send_keys(self.email)
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_password_send_keys).send_keys(self.password)
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_button).click()


   def changing_billing(self):
       self.logger.info('entering billing edit section')
       self.driver.find_element(By.LINK_TEXT, Billing_locators.find_element_LINK_TEXT_adresses).click()
       self.driver.find_element(By.LINK_TEXT,Billing_locators.find_element_LINK_TEXT_edit).click()
       self.logger.info('setting name:Łukasz and lastname:Jagielski')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_name).send_keys('Łukasz')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_lastname).send_keys('Jagielski')
       self.logger.info('setting Austria as billing country')
       auto_select=Select(self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_country))
       auto_select.select_by_visible_text('Austria')
       self.logger.info('setting other city billing adresses')
       self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_address1_send_keys).send_keys('Fabryczna')
       self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_postcode_send_keys).send_keys('1010')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_billing_city_send_keys).send_keys('Wroclaw')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_billing_phone_send_keys).send_keys('352236153')
       self.driver.find_element(By.XPATH,Billing_locators.find_element_XPATH_button_save_address).click()
       self.logger.info('checking if Address is changed successfully')
       assert 'Address changed successfully' in self.driver.find_element(By.XPATH,Billing_locators.find_element_XPATH_woocommerce_message_button).text
