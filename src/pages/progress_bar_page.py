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
        """
        Captura o valor do progresso, garantindo que o texto não esteja vazio.
        """
        progress_text = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.progress_bar).text
        )
        if progress_text.strip():
            return int(progress_text.replace('%', ''))
        return 0

    def wait_until_progress(self, target_percentage):
        """
        Aguarda até que o progresso atinja o valor desejado, garantindo que o texto não esteja vazio.
        """
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_progress_value() >= target_percentage,
            message=f"O progresso não atingiu {target_percentage}% dentro do tempo limite."
        )