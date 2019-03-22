from selenium.webdriver.common.by import By
from .cbr_main_page import CbrMainPage


class CbrWarningPage(CbrMainPage):

    def __init__(self, context):
        CbrMainPage.__init__(
            self,
            context,
            base_url='https://www.cbr.ru/About/warning/')

    locator_dictionary = {
        **CbrMainPage.locator_dictionary,
        "warning": (By.XPATH, '//*[@id="content"]/p')
    }
