import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.web_tables_page import WebTablesPage

class TestWebTables(unittest.TestCase):

    def setUp(self):
        service = Service("C:\\Users\\daiana.santos\\.cache\\selenium\\chromedriver\\win64\\140.0.7339.207\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_web_tables(self):
        # Remove the blocking banner
        self.driver.execute_script("var banner = document.getElementById('fixedban'); if (banner) { banner.remove(); }")

        # Scroll to ensure the element is visible
        elements_section = self.driver.find_element(By.XPATH, "//h5[text()='Elements']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements_section)

        # Navigate to Elements > Web Tables
        elements_section.click()
        web_tables_section = self.driver.find_element(By.XPATH, "//span[text()='Web Tables']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", web_tables_section)
        web_tables_section.click()

        # Interact with Web Tables page
        web_tables_page = WebTablesPage(self.driver)

        # Add a new record
        web_tables_page.add_new_record(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            age="30",
            salary="50000",
            department="Engineering"
        )

        # Edit the record
        web_tables_page.edit_record(first_name="Jane")

        # Delete the record
        web_tables_page.delete_record()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()