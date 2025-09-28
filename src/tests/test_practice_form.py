import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.practice_form_page import PracticeFormPage

class TestPracticeForm(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")

        # Atualizar o caminho para o ChromeDriver
        chromedriver_path = "C:\\Users\\daiana.santos\\.cache\\selenium\\chromedriver\\win64\\140.0.7339.207\\chromedriver.exe"
        service = Service(chromedriver_path)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def test_fill_form(self):
        # Remover iframes de anúncios
        self.driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                iframes[i].remove();
            }
        """)

        # Navegar para o formulário de prática
        forms_section = self.driver.find_element(By.XPATH, "//h5[text()='Forms']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", forms_section)
        forms_section.click()

        practice_form = self.driver.find_element(By.XPATH, "//span[text()='Practice Form']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", practice_form)
        practice_form.click()

        # Interagir com a página do formulário de prática
        practice_form_page = PracticeFormPage(self.driver)
        practice_form_page.fill_form()
        practice_form_page.submit_form()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()