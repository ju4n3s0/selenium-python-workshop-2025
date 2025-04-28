from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_FIELD = (By.ID, 'cb1-edit')
    SEARCH_BUTTON = (By.CLASS_NAME, "nav-search-btn")

    def search(self, text_to_search):
        self.enter_text(self.SEARCH_FIELD, text_to_search)
        time.sleep(3)
        self.click(self.SEARCH_BUTTON)