import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.practice_form_page import PracticeFormPage

class TestPracticeForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        CHROMEDRIVER_PATH = r"C:\Users\daiana.santos\.cache\selenium\chromedriver\win64\136.0.7103.113\chromedriver.exe"
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--load-extension=C:\\Users\\daiana.santos\\Documents\\Desafio\\demoqa\\extensions\\ublock")

        service = Service(CHROMEDRIVER_PATH)
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.practice_form = PracticeFormPage(cls.driver)

    def test_fill_form(self):
        self.practice_form.navigate_to_practice_form()
        self.practice_form.fill_form()
        self.practice_form.submit_form()
        self.practice_form.verify_popup_and_close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()