from selenium.webdriver.common.by import By
from .cbr_main_page import CbrMainPage


class CbrReceptionPage(CbrMainPage):

    def __init__(self, context):
        CbrMainPage.__init__(
            self,
            context,
            base_url='https://www.cbr.ru/Reception/')

    locator_dictionary = {
        **CbrMainPage.locator_dictionary,
        "gratitude_button": (By.XPATH, '//h2[text()="Написать благодарность"]')
    }
