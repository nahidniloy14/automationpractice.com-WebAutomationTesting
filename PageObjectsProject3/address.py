from selenium.webdriver.common.by import By


class page5:
    def __init__(self, driver):  # constructor
        self.driver = driver

    #driver.find_element(By.XPATH, "//button[@class='button btn btn-default button-medium']").click()

    co2=(By.XPATH, "//button[@class='button btn btn-default button-medium']")

    def proceedToCheckoutp5(self):
        return self.driver.find_element(*page5.co2)
