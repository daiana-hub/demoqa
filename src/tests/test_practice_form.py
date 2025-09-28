import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.practice_form_page import PracticeFormPage

class TestPracticeForm(unittest.TestCase):

    def wait_and_remove_ads(self):
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

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # Temporarily disable headless mode for debugging
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")

        # Remove extension loading for simplicity
        # chrome_options.add_argument("--load-extension=c:\\Users\\daiana.santos\\Documents\\Desafio\\demoqa\\extensions\\uBlock0.chromium")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")
        self.wait_and_remove_ads()
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*googlesyndication.com*", "*adservice.google.com*", "*doubleclick.net*"]})
        self.driver.execute_cdp_cmd("Network.enable", {})

    def test_fill_form(self):
        # Navigate to Practice Form
        self.driver.find_element(By.XPATH, "//h5[text()='Forms']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()

        # Interact with Practice Form page
        practice_form_page = PracticeFormPage(self.driver)
        practice_form_page.fill_form()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()