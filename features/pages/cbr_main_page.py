from selenium.webdriver.common.by import By
from .base_page_object import BasePage


class CbrMainPage(BasePage):

    def __init__(self, context, base_url='https://www.cbr.ru/'):
        BasePage.__init__(
            self,
            context.browser,
            base_url=base_url)

    locator_dictionary = {
        "reception_button": (By.XPATH, '//a[text()="Интернет-приемная"]'),
        "warning_link": (By.XPATH, '//a[text()="Предупреждение"]'),
        "burger_button": (By.XPATH, '//div[@id="layout"]//span[@class="burger"]'),
        "about": (By.XPATH, '//*[@class="for_branch_11377"]/a'),
        "en": (By.XPATH, '//a[text()="EN"]')
    }
