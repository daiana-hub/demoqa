import unittest
from selenium import webdriver
from pages.web_tables_page import WebTablesPage

class TestWebTables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_web_tables(self):
        # Navigate to Elements > Web Tables
        self.driver.find_element_by_xpath("//h5[text()='Elements']").click()
        self.driver.find_element_by_xpath("//span[text()='Web Tables']").click()

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