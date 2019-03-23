from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class GoogleMainPage(BasePage):

    def __init__(self, context, base_url='https://www.google.ru/'):
        BasePage.__init__(
            self,
            context,
            base_url=base_url)

    locator_dictionary = {
        "search_input": (By.XPATH, '//input[@title="Поиск"]'),
        "search_button": (By.XPATH, '//*[@class="VlcLAe"]//input[@value="Поиск в Google"]')
    }
