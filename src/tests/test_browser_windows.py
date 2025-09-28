import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.browser_windows_page import BrowserWindowsPage

class TestBrowserWindows(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()

        # Especificar o caminho para o ChromeDriver
        chromedriver_path = "C:\\Users\\daiana.santos\\.cache\\selenium\\chromedriver\\win64\\140.0.7339.207\\chromedriver.exe"
        service = webdriver.chrome.service.Service(chromedriver_path)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/browser-windows")
        self.remove_ads_iframe()

    def remove_ads_iframe(self):
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

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def expand_section(self, section_text):
        """
        Expands a section in the left menu by clicking on its header.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            section_header = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'header-text') and contains(text(), '{section_text}')]"))
            )
            self.scroll_to_element(section_header)
            section_header.click()
        except Exception as e:
            # Save the page source for debugging if the section cannot be expanded
            with open("debug_expand_section.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise e

    def expand_section_with_retry(self, section_text, retries=3):
        """
        Expands a section in the left menu with retries if it fails initially.
        """
        for attempt in range(retries):
            try:
                self.expand_section(section_text)
                return  # Exit if successful
            except Exception as e:
                if attempt < retries - 1:
                    print(f"Retrying to expand section '{section_text}' (Attempt {attempt + 1}/{retries})")
                else:
                    print(f"Failed to expand section '{section_text}' after {retries} attempts.")
                    raise e

    def test_new_window(self):
        # Adicionar espera explícita para garantir que o elemento esteja presente
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 40)  # Aumentar o tempo limite para 40 segundos

        # Remover anúncios ou elementos bloqueadores
        self.driver.execute_script("""
            var ads = document.querySelectorAll('iframe, div[id*="google_ads_iframe"]');
            for (var i = 0; i < ads.length; i++) {
                ads[i].remove();
            }
        """)

        try:
            # Expand the "Alerts, Frame & Windows" section with retries
            self.expand_section_with_retry("Alerts, Frame & Windows")

            # Capturar o HTML da página para depuração antes de localizar o elemento
            with open("debug_before_locating.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            # Garantir que o elemento esteja visível antes de interagir
            alerts_frame_windows = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h5[text()='Alerts, Frame & Windows']"))
            )
            self.scroll_to_element(alerts_frame_windows)
            alerts_frame_windows.click()
        except Exception as e:
            # Capturar o HTML da página para depuração
            with open("debug_error.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise e

        # Continuar com o restante do teste
        new_window_button = wait.until(
            EC.element_to_be_clickable((By.ID, "windowButton"))
        )
        self.scroll_to_element(new_window_button)
        new_window_button.click()

        # Alternar para a nova janela
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Verificar o conteúdo da nova janela
        sample_heading = wait.until(
            EC.presence_of_element_located((By.ID, "sampleHeading"))
        )
        assert sample_heading.text == "This is a sample page", "Texto incorreto na nova janela"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()