from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

#driver.get('http://automationpractice.com/')
driver.get('http://automationpractice.com/index.php?id_product=2&controller=product')
# gives a variable wait
wait = WebDriverWait(driver, 10)
#
#
# def is_signup_visible():
#     element = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="login"]')))
#     return bool(element)

# element = wait.until(EC.visibility_of_any_elements_located('//a[@class="product_img_link"]'))
# element[0].click()

# element = driver.find_element_by_xpath('//select[@id="group_1"]')
element = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="group_1"]')))

drp = Select(element)
drp.select_by_visible_text('M')
