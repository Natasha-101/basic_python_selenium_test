import time


class SignIn():

    def __init__(self, driver):
        self.driver = driver

    def create_new_account(self):
        create_account_button = self.driver.find_element_by_xpath("//*[@class='NlWrkb snByac']")
        create_account_button.click()
        time.sleep(1)
        for_myself = self.driver.find_element_by_xpath("//*[@class = 'jO7h3c']")
        for_myself.click()