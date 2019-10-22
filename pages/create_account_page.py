import time


class CreateAccount():

    def __init__(self, driver):
        self.driver = driver

    def fill_data(self, data):
        first_name_field = self.driver.find_element_by_id("firstName")
        last_name_field = self.driver.find_element_by_id("lastName")
        password_field = self.driver.find_element_by_name("Passwd")
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        username_field = self.driver.find_element_by_id("username")
        first_name_field.send_keys(data['name'])
        last_name_field.send_keys(data['lastname'])
        password_field.send_keys(data['password'])
        confirm_password_field.send_keys(data['password'])
        if 'username' in data:
            username_field.send_keys(data['username'])

    def validate_email(self, email, error=None):
        username_field = self.driver.find_element_by_id("username")
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        username_field.clear()
        username_field.send_keys(email)
        next_button.click()
        if error:
            time.sleep(1)
            assert error in self.driver.page_source