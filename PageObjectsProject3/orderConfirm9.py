from selenium.webdriver.common.by import By


class page9:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # driver.find_element(By.XPATH, "//a[@class='account']/span").click()

    profile=(By.XPATH, "//a[@class='account']/span")

    def visitProfile(self):
        return self.driver.find_element(*page9.profile)
