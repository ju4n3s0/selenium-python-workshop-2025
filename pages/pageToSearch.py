from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class SearchPage(BasePage):
    CORRECT_PAGE = (By.CLASS_NAME , "poly-component__title")

    def isElementPresent(self):
        elemento = self.find_element(self.CORRECT_PAGE)
        text = elemento.text
        return text