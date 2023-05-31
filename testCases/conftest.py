import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from utilities.configReader import getvaluefromconfig


@pytest.fixture(params=["Chrome", "Edge"])
def init_driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(service=ChromeService("Drivers/chromedriver.exe"))
    elif request.param == "Edge":
        driver = webdriver.Edge(service=EdgeService("Drivers/msedgedriver.exe"))
    else:
        driver = webdriver.Chrome(service=ChromeService("Drivers/chromedriver.exe"))
    request.cls.driver = driver
    driver.get(getvaluefromconfig("Parameters", "Application_URL"))
    driver.implicitly_wait(15)
    yield
    driver.quit()
