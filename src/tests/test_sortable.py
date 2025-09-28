import unittest
from selenium import webdriver
from pages.sortable_page import SortablePage

class TestSortable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_sortable(self):
        # Navigate to Interactions > Sortable
        self.driver.find_element_by_xpath("//h5[text()='Interactions']").click()
        self.driver.find_element_by_xpath("//span[text()='Sortable']").click()

        # Interact with Sortable page
        sortable_page = SortablePage(self.driver)

        # Drag and drop items
        sortable_page.drag_and_drop_item(0, 2)  # Move the first item to the third position
        sortable_page.drag_and_drop_item(1, 0)  # Move the second item to the first position

        # Validate the new order
        sorted_items = sortable_page.get_sorted_items_text()
        print("Sorted Items:", sorted_items)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()