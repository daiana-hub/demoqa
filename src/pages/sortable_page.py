from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SortablePage:
    def __init__(self, driver):
        self.driver = driver
        self.sortable_items = (By.CSS_SELECTOR, ".vertical-list-container .list-group-item")  # Atualizei o seletor para localizar os itens corretamente
        self.sortable_container = (By.ID, "sortable")  # Contêiner principal do Sortable

    def drag_and_drop_item(self, source_index, target_index):
        try:
            # Salvar o estado da página antes de localizar o contêiner
            with open("sortable_page_source_before_wait.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            # Aguarde o carregamento completo da página
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Salvar o estado da página antes de localizar o contêiner
            with open("sortable_container_source_before_wait.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            # Aguarde o contêiner principal estar visível
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.sortable_container)
            )

            items = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.sortable_items)
            )
            source = items[source_index]
            target = items[target_index]

            # Garantir que os elementos estejam visíveis na viewport
            self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target)

            actions = ActionChains(self.driver)
            actions.click_and_hold(source).move_to_element(target).release().perform()
        except Exception as e:
            # Salvar o código-fonte da página para depuração
            with open("sortable_page_source_error.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("Erro ao realizar drag and drop:", e)
            raise

    def get_sorted_items_text(self):
        try:
            # Garantir que a tela role até o meio para visibilidade dos elementos
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")

            # Salvar o estado da página antes de localizar os itens
            with open("sortable_items_source_before_wait.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            # Aguarde o carregamento completo da página
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Aguarde o contêiner principal estar visível
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.sortable_container)
            )

            # Localizar os itens ordenáveis
            items = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located(self.sortable_items)
            )
            return [item.text for item in items]
        except Exception as e:
            # Salvar o estado da página em caso de erro
            with open("sortable_items_source_error.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print("Erro ao obter os itens ordenáveis:", e)
            raise