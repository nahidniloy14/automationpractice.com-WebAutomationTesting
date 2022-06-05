from selenium.webdriver.common.by import By


class page2:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # action = ActionChains(driver)
    # hover = driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
    # action.move_to_element(hover).perform()
    #
    # checkout = driver.find_element(By.XPATH, "//div[@class='shopping_cart']/a/span[5]")
    # driver.execute_script("arguments[0].click();", checkout)
