from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_xpath = "//*[@id='Password']"
    button_submit_xpath = "//button[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def getpagetitle(self):
        return self.driver.title

    def enter_user_name(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()
