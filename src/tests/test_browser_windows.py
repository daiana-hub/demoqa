import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.browser_windows_page import BrowserWindowsPage

class TestBrowserWindows(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")
        self.remove_ads_iframe()

    def remove_ads_iframe(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='google_ads_iframe']"))
            )
            self.driver.execute_script("""
                var ads = document.querySelectorAll("iframe[id^='google_ads_iframe']");
                ads.forEach(ad => ad.remove());
            """)
        except TimeoutException:
            pass

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def test_new_window(self):
        # Navigate to Alerts, Frame & Windows > Browser Windows
        alerts_frame_windows = self.driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
        self.scroll_to_element(alerts_frame_windows)
        alerts_frame_windows.click()

        browser_windows = self.driver.find_element(By.XPATH, "//span[text()='Browser Windows']")
        self.scroll_to_element(browser_windows)
        browser_windows.click()

        # Interact with Browser Windows page
        browser_windows_page = BrowserWindowsPage(self.driver)
        browser_windows_page.click_new_window_button()
        browser_windows_page.switch_to_new_window()

        # Validate the message in the new window
        sample_text = browser_windows_page.get_sample_page_text()
        self.assertEqual(sample_text, "This is a sample page")

        # Close the new window
        browser_windows_page.close_current_window()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()