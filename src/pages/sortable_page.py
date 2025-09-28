from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SortablePage:
    def __init__(self, driver):
        self.driver = driver
        self.sortable_items = (By.CSS_SELECTOR, "#sortable li")

    def drag_and_drop_item(self, source_index, target_index):
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.sortable_items)
        )
        source = items[source_index]
        target = items[target_index]

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()

    def get_sorted_items_text(self):
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.sortable_items)
        )
        return [item.text for item in items]