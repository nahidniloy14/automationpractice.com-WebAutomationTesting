from selenium.webdriver.common.by import By


class page10:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # driver.find_element(By.XPATH, "//a[@title='Orders']/span").click()


    od=(By.XPATH, "//a[@title='Orders']/span")

    def orderDetails(self):
        return self.driver.find_element(*page10.od)
