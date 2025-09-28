from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserWindowsPage:
    def __init__(self, driver):
        self.driver = driver
        self.new_window_button = (By.ID, "windowButton")

    def click_new_window_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_window_button)
        ).click()

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break

    def get_sample_page_text(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text

    def close_current_window(self):
        self.driver.close()