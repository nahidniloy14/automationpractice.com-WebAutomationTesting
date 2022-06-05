from selenium.webdriver.common.by import By


class page4:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # driver.find_element(By.ID, "email").send_keys("nahidniloy894@gmail.com")
    # driver.find_element(By.ID, "passwd").send_keys("124634")
    # driver.find_element(By.XPATH, "//div[@class='form_content clearfix']/p[2]/button").click()

    un=(By.ID, "email")
    pwd=(By.ID, "passwd")
    signin=(By.XPATH, "//div[@class='form_content clearfix']/p[2]/button")

    def username(self):
        return self.driver.find_element(*page4.un)
    def passward(self):
        return self.driver.find_element(*page4.pwd)
    def signinbtn(self):
        return self.driver.find_element(*page4.signin)



