from selenium.webdriver.common.by import By


class page8:
    def __init__(self, driver):  # constructor
        self.driver = driver

    #driver.find_element(By.XPATH, "//button[@class='button btn btn-default button-medium']").click()

    confirm=(By.XPATH, "//button[@class='button btn btn-default button-medium']")

    def confirmOrder(self):
        return self.driver.find_element(*page8.confirm)
