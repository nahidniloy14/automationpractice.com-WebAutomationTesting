from selenium.webdriver.common.by import By


class page11:
    def __init__(self, driver):  # constructor
        self.driver = driver


    # driver.find_element(By.LINK_TEXT, "DYUVYCKOZ").click()
    # driver.find_element(By.LINK_TEXT, "Download your invoice as a PDF file.").click()
    # driver.find_element(By.CSS_SELECTOR, ".logout").click()

    ref=(By.XPATH, "//a[@class='account']/span")
    inv=(By.LINK_TEXT, "Download your invoice as a PDF file.")
    lo=(By.CSS_SELECTOR, ".logout")

    def reference(self):
        return self.driver.find_element(*page11.ref)

    def invoice(self):
        return self.driver.find_element(*page11.inv)

    def logout(self):
        return self.driver.find_element(*page11.lo)

