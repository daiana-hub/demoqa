from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SortablePage:
    def __init__(self, driver):
        self.driver = driver
        self.sortable_items = (By.CSS_SELECTOR, "#sortableContainer .vertical-list-container .list-group-item")
        self.sortable_container = (By.ID, "sortableContainer")  # Updated selector for the sortable container
        self.list_tab = (By.ID, "demo-tab-list")  # Selector for the List tab

    def ensure_list_tab_active(self):
        try:
            # Ensure the "List" tab is active
            list_tab_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.list_tab)
            )
            if not list_tab_element.get_attribute("class").__contains__("active"):
                list_tab_element.click()
        except Exception as e:
            print("Error ensuring List tab is active:", e)
            raise

    def remove_ads(self):
        try:
            # Remove ads using JavaScript
            self.driver.execute_script(
                "document.querySelectorAll('[id^=Ad], iframe').forEach(ad => ad.remove());"
            )
        except Exception as e:
            print("Error removing ads:", e)

    def drag_and_drop_item(self, source_index, target_index):
        try:
            self.remove_ads()  # Remove ads before interacting
            self.ensure_list_tab_active()  # Ensure the List tab is active

            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.sortable_container)
            )

            items = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.sortable_items)
            )
            source = items[source_index]
            target = items[target_index]

            self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target)

            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(target).release().perform()
        except Exception as e:
            with open("sortable_page_source_error.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("Error during drag and drop:", e)
            raise

    def get_sorted_items_text(self):
        try:
            self.remove_ads()  # Remove ads before interacting
            self.ensure_list_tab_active()  # Ensure the List tab is active

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.sortable_container)
            )

            items = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(self.sortable_items)
            )
            return [item.text for item in items]
        except Exception as e:
            with open("sortable_items_source_error.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("Error getting sorted items text:", e)
            raise