import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from testCases.BaseTest import BaseTest
from utilities.configReader import getvaluefromconfig


class TestLogin(BaseTest):

    def test_verify_application_title(self):
        self.objlogin = LoginPage(self.driver)
        assert self.objlogin.getpagetitle() == "Your store. Login"


    def test_login_application(self):
        self.objlogin = LoginPage(self.driver)
        self.objlogin.enter_user_name(getvaluefromconfig("Parameters","UserName"))
        self.objlogin.enter_password(getvaluefromconfig("Parameters", "Password"))
        self.objlogin.click_on_login()
