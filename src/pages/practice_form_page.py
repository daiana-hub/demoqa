from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException
import os

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"

    def navigate_to_practice_form(self):
        self.driver.get(self.url)
        forms_element = self.driver.find_element(By.XPATH, "//h5[text()='Forms']")
        self.driver.execute_script("arguments[0].scrollIntoView();", forms_element)
        forms_element.click()
        self.driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()

    def fill_form(self):
        self.driver.find_element(By.ID, "firstName").send_keys("Test")
        self.driver.find_element(By.ID, "lastName").send_keys("User")
        self.driver.find_element(By.ID, "userEmail").send_keys("testuser@example.com")
        self.driver.find_element(By.XPATH, "//label[text()='Male']").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")
        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        self.driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()
        self.driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
        self.driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)
        self.driver.find_element(By.XPATH, "//label[text()='Sports']").click()

        file_path = os.path.join(os.getcwd(), "resources", "sample.txt")
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

        self.driver.find_element(By.ID, "currentAddress").send_keys("123 Test Address")
        
        # Verificar e lidar com iframes que possam bloquear o elemento
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            try:
                self.driver.switch_to.frame(iframe)
                # Verificar se o elemento está visível no iframe
                if self.driver.find_elements(By.ID, "state"):
                    break
            except Exception:
                continue
        self.driver.switch_to.default_content()

        # Rolar até o elemento antes de clicar
        state_element = self.driver.find_element(By.ID, "state")
        self.driver.execute_script("arguments[0].scrollIntoView();", state_element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "state")))
        state_element.click()

        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()

    def verify_popup_and_close(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "closeLargeModal"))
        )
        close_button = self.driver.find_element(By.ID, "closeLargeModal")
        self.driver.execute_script("arguments[0].scrollIntoView();", close_button)
        close_button.click()

    def switch_to_main_content(self):
        try:
            self.driver.switch_to.default_content()
        except NoSuchFrameException:
            pass

    def remove_ads_iframe(self):
        self.switch_to_main_content()
        try:
            ad_iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[id^='google_ads_iframe']")
            self.driver.switch_to.frame(ad_iframe)
            self.driver.execute_script("document.body.innerHTML = '';")
            self.switch_to_main_content()
        except NoSuchElementException:
            pass