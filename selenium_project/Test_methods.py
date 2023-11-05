from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service()
options = webdriver.ChromeOptions()
from selenium.webdriver.support.select import Select
from locators import Billing_locators
import random
class test_change_billing:
   def __init__(self,driver):
       self.email = str(random.randint(1, 10000)) + 'exlares@gmail.com'
       self.password = str(random.randint(1, 10000)) + 'Xilla122@@'
       self.driver = driver



   def sing_up(self):
       self.driver.get('http://seleniumdemo.com/')
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_myAccount).click()
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_email).send_keys(self.email)
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_password_send_keys).send_keys(self.password)
       self.driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_button).click()


   def changing_billing(self):
       self.driver.find_element(By.LINK_TEXT, Billing_locators.find_element_LINK_TEXT_adresses).click()
       self.driver.find_element(By.LINK_TEXT,Billing_locators.find_element_LINK_TEXT_edit).click()
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_name).send_keys('Łukasz')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_lastname).send_keys('Jagielski')
       auto_select=Select(self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_country))
       auto_select.select_by_visible_text('Austria')
       self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_address1_send_keys).send_keys('Fabryczna')
       self.driver.find_element(By.ID,Billing_locators.find_element_ID_billing_postcode_send_keys).send_keys('1010')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_billing_city_send_keys).send_keys('Wroclaw')
       self.driver.find_element(By.ID, Billing_locators.find_element_ID_billing_phone_send_keys).send_keys('352236153')
       self.driver.find_element(By.XPATH,Billing_locators.find_element_XPATH_button_save_address).click()
       assert 'Address changed successfully' in self.driver.find_element(By.XPATH,Billing_locators.find_element_XPATH_woocommerce_message_button).text