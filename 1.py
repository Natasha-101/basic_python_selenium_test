from selenium import webdriver

import time
driver = webdriver.Chrome('D:\Наташенька\PYTHON\chromedriver.exe')
driver.implicitly_wait(10)

driver.get("https://accounts.google.com")

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

time.sleep(2)

for_myself_button = driver.find_element_by_xpath("//*[text()='Для себя']")
for_myself_button.click()


first_name_field = driver.find_element_by_id("firstName")

first_name_field.send_keys("Natasha")
last_name_field = driver.find_element_by_id("lastName")
last_name_field.send_keys("Butenko")

password_field = driver.find_element_by_name("Passwd")
password_field.send_keys("1234567by")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
confirm_password_field.send_keys("1234567by")

username_field = driver.find_element_by_id("username")
username_field.clear()
username_field.send_keys("123Nataby123")

next_button = driver.find_element_by_id("accountDetailsNext")
next_button.click()

assert "Natasha12345!" in driver.page_source

driver.quit()
