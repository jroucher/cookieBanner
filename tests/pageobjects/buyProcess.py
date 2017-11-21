# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class BuyProcessPageObject(PageObject):
	viewCart = ""
	
	def init_page_elements(self):
		return self;

	def setElements(self):
		self.addButton = Button(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[3]')
		self.nameItem = ""
		return self;

	def open(self, sectionName = None):
		""" Open app url in browser
		:returns: this page object instance
		"""
		url = self.config.get('Common', 'url')
		self.driver.get(url)
		return self

	def waitToDrawHome(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[2]/figure/img').locator)
		return self

	def waitToDrawCart(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="post-5"]/header/h2/b').locator)
		return self

	def waitToDrawCheckout(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="post-6"]/header/h2').locator)
		return self
	
	def waitToDrawPay(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="bodyContent"]').locator)
		return self
		
	def waitToDrawSomeMoreData(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="dni"]').locator)
		return self
		
	def addItemToCart(self):
		
		self.addButton = Button(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[3]')
		self.addButton.click()
		self.nameItem = Text(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[2]/h3')
		viewCart = Button(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[4]')
		self.utils.wait_until_element_visible(viewCart.locator)
		return self

	def goToCart(self):
		viewCart = Button(By.XPATH, '//*[@id="primary"]/ul/li[1]/a[4]')
		viewCart.click()
		return self
	
	def itemPresent(self):
		self.utils.wait_until_element_visible(Text(By.XPATH, '//*[@id="post-5"]/div[2]/div/form/table/tbody/tr[1]/td[2]/a/img').locator)
		return self
	
	def checkout(self):
		self.driver.find_elements_by_class_name("checkout-button")[0].click()
		return self
		
		
	def typeForm(self):
		self.driver.find_elements_by_id('billing_first_name')[0].send_keys('Name')
		self.driver.find_elements_by_id('billing_last_name')[0].send_keys('lastName')
		self.driver.find_elements_by_id( 'billing_email')[0].send_keys('email@email.com')
		self.driver.find_elements_by_id('billing_phone')[0].send_keys('666666666')
		self.driver.find_elements_by_id('billing_address_1')[0].send_keys('c\ mi casa')
		self.driver.find_elements_by_id('billing_address_2')[0].send_keys('numero 2')
		self.driver.find_elements_by_id('billing_postcode')[0].send_keys('28000')
		self.driver.find_elements_by_id('billing_city')[0].send_keys('Madrid')
		
		time.sleep( 1 ) # wait for page to render    
		dropdown = self.driver.find_element(By.XPATH, '//*[@id="select2-chosen-2"]')
		dropdown.click()
		time.sleep( 1 ) # probably not necessary
		option   = self.driver.find_element(By.XPATH, '//*[@id="s2id_autogen2_search"]')
		option.click()
		time.sleep( 1 )	# probably not necessary	
		option.send_keys('Madrid')
		time.sleep( 1 ) # wait for page to render
		option.send_keys(Keys.RETURN)
		time.sleep( 1 ) # probably not necessary

		Button(By.XPATH, '//*[@id="place_order"]').click()
		return self
		
	def pay(self):
		time.sleep( 5 ) # wait for redirect    
		ok = Button(By.XPATH, '//*[@id="bodyContent"]/div/div/div/div[1]/form/div[2]/div/div/label/span[1]')
		ok.click()
		submit = Button(By.XPATH, '//*[@id="FlexibleForm-submitButton"]')
		submit.click()
		return self
		
		
	def MoreData(self):
		time.sleep( 1 ) # probably not necessary
		self.driver.find_elements_by_id('dni')[0].send_keys('11111111h')
		return self
	
	
	