from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import traceback
import time


class BasePage(object):

    def __init__(self, browser, base_url='http://www.seleniumframework.com'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 10

    def go_to_last_page(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self):
        self.browser.get(self.base_url)

    def screenshot(self, context):
        context.screenshots.append(self.browser.get_screenshot_as_png())

    def assert_page(self, url):
        current_ps = self.browser.page_source
        self.browser.get("http://" + url)
        expected_ps = self.browser.page_source
        assert (current_ps != expected_ps)

    def hover(self, element):
            ActionChains(self.browser).move_to_element(element).perform()
            # I don't like this but hover is sensitive and needs some sleep time
            time.sleep(5)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        ec.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        ec.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what)
