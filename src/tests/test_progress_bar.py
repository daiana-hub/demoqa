import unittest
from selenium import webdriver
from pages.progress_bar_page import ProgressBarPage

class TestProgressBar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_progress_bar(self):
        # Navigate to Widgets > Progress Bar
        self.driver.find_element_by_xpath("//h5[text()='Widgets']").click()
        self.driver.find_element_by_xpath("//span[text()='Progress Bar']").click()

        # Interact with Progress Bar page
        progress_bar_page = ProgressBarPage(self.driver)

        # Start the progress bar
        progress_bar_page.click_start()

        # Stop before 25%
        progress_bar_page.wait_until_progress(25)
        progress_bar_page.click_stop()

        # Validate progress is <= 25%
        progress = progress_bar_page.get_progress_value()
        self.assertLessEqual(progress, 25, "Progress is greater than 25%")

        # Start again and wait until 100%
        progress_bar_page.click_start()
        progress_bar_page.wait_until_progress(100)

        # Reset the progress bar
        progress_bar_page.click_reset()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()