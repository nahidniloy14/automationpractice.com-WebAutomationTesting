from selenium.webdriver.common.by import By


class page1:
    def __init__(self, driver):  # constructor
        self.driver = driver

    sp1 = (By.XPATH, "//a[@data-id-product='6']/span")
    cons = (By.XPATH, "//span[@class='continue btn btn-default button exclusive-medium']")
    sp2 = (By.XPATH, "//a[@data-id-product='4']/span")
    co = (By.XPATH, "//a[@title='Proceed to checkout']")

    def product1(self):
        return self.driver.find_element(*page1.sp1)

    def continueShopping(self):
        return self.driver.find_element(*page1.cons)

    def product2(self):
        return self.driver.find_element(*page1.sp2)

    def checkout(self):
        return self.driver.find_element(*page1.co)
