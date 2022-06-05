
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from setuptools import logging

import pytest
from seleniumBasics.main import driver


@pytest.mark.usefixtures("setup")
class subClass:
    def getlogger(self):
        # loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(__name__)  # method to log everything#__name__ prints name
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # accept filehandler object #logger format and file
        logger.setLevel(logging.DEBUG)
        # logger.debug("debug executed")
        # logger.info("Information: ")
        # logger.warning("Warnings: ")
        # logger.error("a major error has occured")
        # logger.critical("Critical Issue")



    def waitTillElementLocated(self, locator, XPathlocation):
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located((locator, XPathlocation))).click()

    def performHover(self,locator,location):
        action = ActionChains(driver)
        hover = driver.find_elemnet(locator,location)
        action.move_to_element(hover).perform()

    def usingJS(self,locator,location):
        checkout = driver.find_element(locator,location)
        driver.execute_script("arguments[0].click();", checkout)


