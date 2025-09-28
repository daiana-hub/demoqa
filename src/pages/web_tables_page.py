from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.ID, "addNewRecordButton")
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.age_input = (By.ID, "age")
        self.salary_input = (By.ID, "salary")
        self.department_input = (By.ID, "department")
        self.submit_button = (By.ID, "submit")
        self.edit_button = (By.CSS_SELECTOR, "span[title='Edit']")
        self.delete_button = (By.CSS_SELECTOR, "span[title='Delete']")

    def add_new_record(self, first_name, last_name, email, age, salary, department):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.age_input).send_keys(age)
        self.driver.find_element(*self.salary_input).send_keys(salary)
        self.driver.find_element(*self.department_input).send_keys(department)
        self.driver.find_element(*self.submit_button).click()

    def edit_record(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_button)
        ).click()
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.submit_button).click()

    def delete_record(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()