import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.sortable_page import SortablePage

class TestSortable(unittest.TestCase):

    def setUp(self):
        chromedriver_path = "C:\\Users\\daiana.santos\\.cache\\selenium\\chromedriver\\win64\\140.0.7339.207\\chromedriver.exe"
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def remove_blocking_elements(self):
        """
        Remove elementos bloqueadores, como banners fixos, que podem interceptar cliques.
        """
        try:
            self.driver.execute_script("""
                var banners = document.querySelectorAll('#fixedban, iframe[id^=\"google_ads_iframe\"]');
                banners.forEach(banner => banner.remove());
            """)
        except Exception as e:
            print("Erro ao remover elementos bloqueadores:", e)

    def scroll_into_view(self, element):
        """
        Scroll the given element into view.
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def test_sortable(self):
        # Remover banners ou elementos bloqueadores
        self.remove_blocking_elements()

        # Navegar para Interactions > Sortable
        interactions_element = self.driver.find_element(By.XPATH, "//h5[text()='Interactions']")
        self.scroll_into_view(interactions_element)  # Ensure the element is visible
        interactions_element.click()

        sortable_element = self.driver.find_element(By.XPATH, "//span[text()='Sortable']")
        self.scroll_into_view(sortable_element)  # Ensure the element is visible
        sortable_element.click()

        # Criar a instância de SortablePage
        sortable_page = SortablePage(self.driver)

        # Garantir que a tela role até o meio para visibilidade dos elementos
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")

        # Obter os textos dos itens antes de ordenar
        original_items = sortable_page.get_sorted_items_text()

        # Verificar se os itens já estão em ordem crescente
        if original_items != sorted(original_items):
            sorted_items = sorted(original_items)  # Ordenar os textos em ordem crescente

            # Reorganizar os itens na ordem crescente verticalmente
            for current_index, item_text in enumerate(sorted_items):
                target_index = original_items.index(item_text)
                if target_index != current_index:  # Mover apenas se necessário
                    sortable_page.drag_and_drop_item(target_index, current_index)

            # Validar a nova ordem
            final_items = sortable_page.get_sorted_items_text()
            assert final_items == sorted_items, f"Itens não estão em ordem crescente: {final_items}"
        else:
            print("Os itens já estão em ordem crescente.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()