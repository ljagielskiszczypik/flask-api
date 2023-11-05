import time

import pytest
import logging
import random
from locators import Billing_locators
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get('http://seleniumdemo.com/')
driver.maximize_window()
driver.implicitly_wait(10)

email = str(random.randint(1, 10000)) + 'exlares@gmail.com'
password = str(random.randint(1, 10000)) + 'Xilla122@@'

driver.get('http://seleniumdemo.com/')
driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_myAccount).click()
driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_email).send_keys(email)
driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_password_send_keys).send_keys(password)
driver.find_element(By.XPATH, Billing_locators.find_element_XPATH_button).click()


driver.find_element(By.LINK_TEXT, Billing_locators.find_element_LINK_TEXT_adresses).click()
driver.find_element(By.LINK_TEXT,Billing_locators.find_element_LINK_TEXT_edit).click()

driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_name).send_keys('Łukasz')
driver.find_element(By.ID, Billing_locators.find_element_ID_send_keys_lastname).send_keys('Jagielski')

auto_select=Select(driver.find_element(By.ID,Billing_locators.find_element_ID_billing_country))
auto_select.select_by_visible_text('Austria')

driver.find_element(By.ID,Billing_locators.find_element_ID_billing_address1_send_keys).send_keys('Fabryczna')
driver.find_element(By.ID,Billing_locators.find_element_ID_billing_postcode_send_keys).send_keys('1010')
driver.find_element(By.ID, Billing_locators.find_element_ID_billing_city_send_keys).send_keys('Wroclaw')
driver.find_element(By.ID, Billing_locators.find_element_ID_billing_phone_send_keys).send_keys('352236153')
driver.find_element(By.XPATH,Billing_locators.find_element_XPATH_button_save_address).click()
time.sleep(5)

driver.quit()