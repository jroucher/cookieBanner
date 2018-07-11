# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *

class cookiebannerPageObject(PageObject):

    def init_page_elements(self):
        return self

    def waitToDrawHome (self):
        menu = Text(By.XPATH, '//*[@id="hs_menu_wrapper_module_14696293048515"]/ul/li[5]/a')
        self.utils.wait_until_element_visible(menu)
        self.menu = menu
        return self

    def open(self, sectionName = None):
        """ Open app url in browser
        :returns: this page object instance
        """
        url = self.config.get('Common', 'url')
        self.driver.get(url)
        return self

    def cookieTitlePresent(self):
        cookieTitle = Text(By.XPATH, '//*[@id="hs-eu-cookie-confirmation-inner"]/div[2]')
        self.utils.wait_until_element_visible(cookieTitle, 10)
        self.cookieTitle = cookieTitle
        return self

    def cookieTextPresent(self):
        cookieText = Text(By.XPATH, '//*[@id="hs-eu-cookie-confirmation-inner"]/p[2]')
        self.utils.wait_until_element_visible(cookieText, 10)
        self.cookieText = cookieText
        return self

    def cookieButtonsPresent(self):
        cookieButtonA = Button(By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
        cookieButtonD = Text(By.XPATH, '//*[@id="hs-eu-decline-button"]')
        self.utils.wait_until_element_visible(cookieButtonA, 10)
        self.utils.wait_until_element_visible(cookieButtonD, 10)
        self.cookieButtonA = cookieButtonA
        self.cookieButtonD = cookieButtonD
        return self

    def acceptCookieButton(self):
        cookieButtonA = Button(By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
        self.utils.wait_until_element_visible(cookieButtonA, 10)
        self.cookieButtonA = cookieButtonA
        self.cookieButtonA.click()
        return self

    def cookieTitleNotVisible(self):
        cookieTitle = Text(By.XPATH, '//*[@id="hs-eu-cookie-confirmation-inner"]/div[2]')
        self.utils.wait_until_element_not_visible(cookieTitle, 10)
        self.cookieTitle = cookieTitle
        return self

    def cookieTextNotVisible(self):
        cookieText = Text(By.XPATH, '//*[@id="hs-eu-cookie-confirmation-inner"]/p[2]')
        self.utils.wait_until_element_not_visible(cookieText, 10)
        self.cookieText = cookieText
        return self

    def cookieButtonsNotVisible(self):
        cookieButtonA = Button(By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
        cookieButtonD = Text(By.XPATH, '//*[@id="hs-eu-decline-button"]')
        self.utils.wait_until_element_not_visible(cookieButtonA, 10)
        self.utils.wait_until_element_not_visible(cookieButtonD, 10)
        self.cookieButtonA = cookieButtonA
        self.cookieButtonD = cookieButtonD
        return self