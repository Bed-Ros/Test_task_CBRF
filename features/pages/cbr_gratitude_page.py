from selenium.webdriver.common.by import By
from .cbr_main_page import CbrMainPage


class CbrGratitudePage(CbrMainPage):

    def __init__(self, context):
        CbrMainPage.__init__(
            self,
            context.browser,
            base_url='https://www.cbr.ru/Reception/Message/Register?messageType=Gratitude')

    locator_dictionary = {
        **CbrMainPage.locator_dictionary,
        "message_input": (By.ID, 'MessageBody'),
        "agreement_flag": (By.ID, '_agreementFlag')
    }
