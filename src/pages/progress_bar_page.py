from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProgressBarPage:
    def __init__(self, driver):
        self.driver = driver
        self.start_stop_button = (By.ID, "startStopButton")
        self.reset_button = (By.ID, "resetButton")
        self.progress_bar = (By.CLASS_NAME, "progress-bar")

    def click_start(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_stop_button)
        ).click()

    def click_stop(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_stop_button)
        ).click()

    def click_reset(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reset_button)
        ).click()

    def get_progress_value(self):
        progress_text = self.driver.find_element(*self.progress_bar).text
        return int(progress_text.replace('%', ''))

    def wait_until_progress(self, target_percentage):
        while True:
            progress = self.get_progress_value()
            if progress >= target_percentage:
                break
            time.sleep(0.1)