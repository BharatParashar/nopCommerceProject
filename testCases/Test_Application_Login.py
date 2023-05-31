import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from testCases.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_verify_application_title(self):
        self.objlogin = LoginPage(self.driver)
        assert self.objlogin.getpagetitle() == "Your store. Login"
