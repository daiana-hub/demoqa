from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"

    def navigate_to_practice_form(self):
        self.driver.get(self.url)
        forms_element = self.driver.find_element(By.XPATH, "//h5[text()='Forms']")
        self.driver.execute_script("arguments[0].scrollIntoView();", forms_element)
        forms_element.click()
        self.driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()

    def fill_form(self):
        # Garantir que os elementos estão visíveis antes de interagir
        first_name = self.driver.find_element(By.ID, "firstName")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_name)
        first_name.send_keys("Test")

        last_name = self.driver.find_element(By.ID, "lastName")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", last_name)
        last_name.send_keys("User")

        email = self.driver.find_element(By.ID, "userEmail")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email)
        email.send_keys("testuser@example.com")

        self.driver.find_element(By.XPATH, "//label[text()='Male']").click()

        phone = self.driver.find_element(By.ID, "userNumber")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", phone)
        phone.send_keys("1234567890")

        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        self.driver.find_element(By.CLASS_NAME, "react-datepicker__day--015").click()

        subjects = self.driver.find_element(By.ID, "subjectsInput")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", subjects)
        subjects.send_keys("Maths")
        subjects.send_keys(Keys.RETURN)

        # Remover anúncios antes de clicar no checkbox
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, div[id*="google_ads_iframe"]');
            for (var i = 0; i < ads.length; i++) {
                ads[i].remove();
            }
        """)

        # Usar JavaScript para clicar no checkbox
        sports_checkbox = self.driver.find_element(By.XPATH, "//label[text()='Sports']")
        self.driver.execute_script("arguments[0].click();", sports_checkbox)

        # Corrigir o caminho do arquivo para upload
        file_path = os.path.join(os.getcwd(), "resources", "sample.txt")
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

        # Garantir que o campo 'Current Address' está visível e interativo
        try:
            wait = WebDriverWait(self.driver, 10)
            address = wait.until(EC.visibility_of_element_located((By.ID, "currentAddress")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address)
            address.clear()
            address.send_keys("123 Test Address")
            print("Campo 'Current Address' preenchido com sucesso.")
        except TimeoutException:
            print("Erro: O campo 'Current Address' não está visível ou não foi encontrado.")
            return

        # Garantir que o elemento 'state' está visível e usar JavaScript para clicar
        state_element = self.driver.find_element(By.ID, "state")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_element)
        self.driver.execute_script("arguments[0].click();", state_element)

        # Adicionar espera explícita para o dropdown abrir
        try:
            dropdown_open = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'menu')]")))
            print("Dropdown de estado aberto com sucesso.")
        except TimeoutException:
            print("Erro: O dropdown de estado não foi aberto.")
            return

        # Garantir que o elemento 'NCR' está visível antes de clicar
        try:
            ncr_element = self.driver.find_element(By.XPATH, "//div[text()='NCR']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ncr_element)
            ncr_element.click()
        except Exception as e:
            print(f"Erro ao localizar ou clicar no elemento NCR: {e}")
            return

        city_element = self.driver.find_element(By.ID, "city")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city_element)
        self.driver.execute_script("arguments[0].click();", city_element)

        # Adicionar espera explícita para o dropdown abrir
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Delhi']")))
            delhi_element = self.driver.find_element(By.XPATH, "//div[text()='Delhi']")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delhi_element)
            delhi_element.click()
        except TimeoutException:
            print("Erro: O elemento 'Delhi' não foi encontrado ou não está visível.")

    def submit_form(self):
        try:
            # Garantir que o botão 'submit' está visível
            submit_button = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)

            # Remover elementos bloqueadores
            self.driver.execute_script("""
                var blockers = document.querySelectorAll('div, iframe');
                for (var i = 0; i < blockers.length; i++) {
                    if (blockers[i].style.position === 'fixed' || blockers[i].style.zIndex > 1000) {
                        blockers[i].remove();
                    }
                }
            """)

            # Tentar clicar no botão
            try:
                submit_button.click()
                print("Botão 'submit' clicado com sucesso.")
            except Exception as e:
                print(f"Erro ao clicar no botão 'submit': {e}")
                # Fallback: Usar JavaScript para clicar
                self.driver.execute_script("arguments[0].click();", submit_button)
                print("Botão 'submit' clicado usando JavaScript.")
        except TimeoutException:
            print("Erro: O botão 'submit' não está visível ou não foi encontrado.")