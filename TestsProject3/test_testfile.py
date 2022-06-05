from selenium.webdriver.common.by import By
from seleniumProject3.PageObjectsProject3.addToCart1 import page1
from seleniumProject3.PageObjectsProject3.address import page5
from seleniumProject3.PageObjectsProject3.myAccount import page10
from seleniumProject3.PageObjectsProject3.orderConfirm9 import page9
from seleniumProject3.PageObjectsProject3.orderHistory11 import page11
from seleniumProject3.PageObjectsProject3.orderSumamry8 import page8
from seleniumProject3.PageObjectsProject3.shipping6 import page6
from seleniumProject3.PageObjectsProject3.signIn import page4
from seleniumProject3.UtilitiesProject3.subClass import subClass


class TestCase1(subClass):
    def test_main(self):
        log = self.getlogger()

        # addToCart1
        ob1 = page1(self.driver)
        ob1.product1().click()
        ob2 = page1(self.driver)
        ob2.continueShopping().click()
        ob3 = page1(self.driver)
        ob3.product2().click()
        ob4 = page1(self.driver)
        ob4.checkout().click()

        # selectCart2
        self.performHover(By.XPATH, "//a[@title='View my shopping cart']")
        self.usingJS(By.XPATH, "//div[@class='shopping_cart']/a/span[5]")

        # sumamry3

        self.waitTillElementLocated(By.XPATH, "//p[@class='cart_navigation clearfix']/a/span")
        log.info("Test Case 1 Passed")

        # signin4
        ob5 = page4(self.driver)
        ob5.username().send_keys("nahidniloy894@gmail.com")
        ob6 = page4(self.driver)
        ob6.passward().send_keys("124634")
        ob7 = page4(self.driver)
        ob7.signinbtn().click()

        # address5
        ob8 = page5(self.driver)
        ob8.proceedToCheckoutp5().click()

        # shipping6
        ob9 = page6(self.driver)
        ob9.radiobutton().click()
        ob10 = page6(self.driver)
        ob10.proceedTocheckoutp6().click()

        # payment7
        self.waitTillElementLocated(By.XPATH, "//a[@class='cheque']")

        log.info("Test Case 2 Passed")

        # orderSummary8
        ob10 = page8(self.driver)
        ob10.confirmOrder().click()

        # orderConfirm9
        ob11 = page9(self.driver)
        ob11.visitProfile().click()

        # myAccount10
        ob12 = page10(self.driver)
        ob12.orderDetails().click()

        # orderHistory11
        ob13 = page11(self.driver)
        ob13.reference().click()

        ob14 = page11(self.driver)
        ob14.invoice().click()

        ob15 = page11(self.driver)
        ob15.logout().click()

        log.info("Test Case 3 Passed")
