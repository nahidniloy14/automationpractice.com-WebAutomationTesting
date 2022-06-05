from selenium.webdriver.common.by import By


class page6:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CSS_SELECTOR, "#cgv").click()
    # driver.find_element(By.XPATH,
    #                     "//button[@class='button btn btn-default standard-checkout button-medium']").click()
    rb = (By.CSS_SELECTOR, "#cgv")
    co3 = (By.XPATH, "//button[@class='button btn btn-default standard-checkout button-medium']")

    def radiobutton(self):
        return self.driver.find_element(*page6.rb)

    def proceedTocheckoutp6(self):
        return self.driver.find_element(*page6.co3)
