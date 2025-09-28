import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.progress_bar_page import ProgressBarPage

class TestProgressBar(unittest.TestCase):

    def setUp(self):
        chromedriver_path = "C:\\Users\\daiana.santos\\.cache\\selenium\\chromedriver\\win64\\140.0.7339.207\\chromedriver.exe"
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

    def remove_ads_iframe(self):
        """
        Remove iframes de anúncios que podem bloquear interações.
        """
        try:
            self.driver.execute_script("""
                var ads = document.querySelectorAll('iframe[id^="google_ads_iframe"]');
                ads.forEach(ad => ad.remove());
            """)
        except Exception as e:
            print("Erro ao remover iframes de anúncios:", e)

    def remove_blocking_elements(self):
        """
        Remove elementos bloqueadores, como anúncios, que podem interceptar cliques.
        """
        try:
            self.driver.execute_script("""
                var ads = document.querySelectorAll('#adplus-anchor, iframe[id^="google_ads_iframe"]');
                ads.forEach(ad => ad.remove());
            """)
        except Exception as e:
            print("Erro ao remover elementos bloqueadores:", e)

    def scroll_to_element(self, element):
        """
        Realiza o scroll até o elemento para garantir que ele esteja visível.
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def test_progress_bar(self):
        # Remover anúncios ou elementos bloqueadores
        self.remove_blocking_elements()

        # Navegar para Widgets > Progress Bar
        widgets_element = self.driver.find_element(By.XPATH, "//h5[text()='Widgets']")
        self.scroll_to_element(widgets_element)
        widgets_element.click()

        progress_bar_element = self.driver.find_element(By.XPATH, "//span[text()='Progress Bar']")
        self.scroll_to_element(progress_bar_element)
        progress_bar_element.click()

        # Interagir com a página de Progress Bar
        progress_bar_page = ProgressBarPage(self.driver)

        # Iniciar o progress bar
        progress_bar_page.click_start()

        # Parar antes de 25% (ajustado para parar mais cedo)
        progress_bar_page.wait_until_progress(20)
        progress_bar_page.click_stop()

        # Validar que o progresso é <= 25%
        progress = progress_bar_page.get_progress_value()
        self.assertLessEqual(progress, 25, "Progress is greater than 25%")

        # Iniciar novamente e esperar até 100%
        progress_bar_page.click_start()
        progress_bar_page.wait_until_progress(100)

        # Resetar o progress bar
        progress_bar_page.click_reset()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()