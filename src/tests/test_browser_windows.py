import unittest
from selenium import webdriver
from pages.browser_windows_page import BrowserWindowsPage

class TestBrowserWindows(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_new_window(self):
        # Navigate to Alerts, Frame & Windows > Browser Windows
        self.driver.find_element_by_xpath("//h5[text()='Alerts, Frame & Windows']").click()
        self.driver.find_element_by_xpath("//span[text()='Browser Windows']").click()

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