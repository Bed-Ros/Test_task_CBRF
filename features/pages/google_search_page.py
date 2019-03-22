from selenium.webdriver.common.by import By
from .google_main_page import GoogleMainPage


class GoogleSearchPage(GoogleMainPage):

    locator_dictionary = {
        **GoogleMainPage.locator_dictionary,
        "search_button": (By.CLASS_NAME, 'z1asCe MZy1Rb'),
        "link_cbr_ru": (By.LINK_TEXT, 'cbr.ru')
    }
