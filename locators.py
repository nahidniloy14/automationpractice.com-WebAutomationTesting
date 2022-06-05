from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(5)
#driver.maximize_window()
# html = driver.find_element(By.TAG_NAME,'html')
# html.send_keys(Keys.END)
# driver.execute_script("window.scrollTo(0,1200);")
driver.find_element(By.XPATH, "//a[@data-id-product='6']/span").click()
driver.find_element(By.XPATH, "//span[@class='continue btn btn-default button exclusive-medium']").click()
driver.find_element(By.XPATH, "//a[@data-id-product='4']/span").click()
driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']").click()

action = ActionChains(driver)
hover = driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
action.move_to_element(hover).perform()

checkout = driver.find_element(By.XPATH, "//div[@class='shopping_cart']/a/span[5]")
driver.execute_script("arguments[0].click();", checkout)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# get element  after explicitly waiting for 10 seconds
# driver.find_element(By.XPATH,"//tr[@class='cart_total_price']/td[2]/span").get_attribute('value')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait = WebDriverWait(driver,60)
wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='cart_navigation clearfix']/a/span"))).click()
# driver.find_element(By.CSS_SELECTOR,"#email_create").send_keys("nahidniloy894@gmail.com")
# driver.find_element(By.XPATH,"//div[@class='form_content clearfix']/div[3]/button").click()
# driver.find_element(By.CSS_SELECTOR,"#id_gender1").click()
# driver.find_element(By.CSS_SELECTOR,"#customer_firstname").send_keys("Nahid Hassan")
# driver.find_element(By.CSS_SELECTOR,"#customer_lastname").send_keys("Niloy")
# driver.find_element(By.CSS_SELECTOR,"#passwd").send_keys("124634")
# driver.find_element(By.XPATH,"//div[@class='col-xs-4']/div/select[1]/option[21]").click()
# driver.find_element(By.XPATH,"//select[@id='months']/option[10]").click()
#
# years=driver.find_element(By.XPATH,"//select[@id='years']/option[28]").click()
# driver.find_element(By.CSS_SELECTOR,"#company").send_keys("Automation Solutionzz")
# driver.find_element(By.CSS_SELECTOR,"#address1").send_keys("1011/1 South Ibrahimpur")
# driver.find_element(By.CSS_SELECTOR,"#city").send_keys("Bahamas")
# #driver.find_element(By.XPATH,"//select[@id='id_state']/option[5]")
# states=driver.find_elements(By.XPATH,"//select[@id='id_state']/option")
# for i in states:
#     if i.text == "California":
#         i.click()
#         break
# driver.find_element(By.CSS_SELECTOR,"#postcode").send_keys("14141")
# driver.find_element(By.CSS_SELECTOR,"#phone_mobile").send_keys("01712970440")
# driver.find_element(By.CSS_SELECTOR,"#alias").send_keys("Ibrahimpur")
# driver.find_element(By.XPATH,"//div[@class='submit clearfix']/button").click()

driver.find_element(By.ID,"email").send_keys("nahidniloy894@gmail.com")
driver.find_element(By.ID,"passwd").send_keys("124634")
driver.find_element(By.XPATH,"//div[@class='form_content clearfix']/p[2]/button").click()
driver.find_element(By.XPATH,"//button[@class='button btn btn-default button-medium']").click()
driver.find_element(By.CSS_SELECTOR,"#cgv").click()
driver.find_element(By.XPATH,"//button[@class='button btn btn-default standard-checkout button-medium']").click()
driver.find_element(By.XPATH,"//tr[@class='cart_total_price']/td[2]/span").get_attribute('id')
wait = WebDriverWait(driver,60)
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='cheque']"))).click()
driver.find_element(By.XPATH,"//p[@class='cart_navigation clearfix']/button").click()
driver.find_element(By.XPATH,"//a[@class='account']/span").click()
driver.find_element(By.XPATH,"//a[@title='Orders']/span").click()
driver.find_element(By.LINK_TEXT,"DYUVYCKOZ").click()
driver.find_element(By.LINK_TEXT,"Download your invoice as a PDF file.").click()
driver.find_element(By.CSS_SELECTOR,".logout").click()

#maximize window problem