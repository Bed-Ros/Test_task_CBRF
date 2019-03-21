#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@Given('Зашли на сайт "{url}"')
def step(context, url):
    context.browser.get("http://" + url)


@Then('Проверили, что появилось поле "{title}"')
def step(context, title):
    locator = (By.XPATH, f'//input[@title="{title}"]')
    wait(context.browser, 10).until(
        ec.presence_of_element_located(locator))
    context.google_search_el = context.browser.find_element(*locator)


@When('Ввели в поле Поиск значение "{text}"')
def step(context, text):
    context.google_search_el.send_keys(text)


@When('Нажали на кнопку "Поиск в Google"')
def step(context):
    locator = (By.XPATH, '//*[@id="tsf"]/div[2]/div/div[2]/div[2]/div/center/input[1]')
    wait(context.browser, 1).until(
        ec.element_to_be_clickable(locator))
    context.browser.find_element(*locator).click()


@Then('Нашли ссылку "{url}"')
def step(context, url):
    locator = (By.PARTIAL_LINK_TEXT, url)
    wait(context.browser, 10).until(
        ec.presence_of_element_located(locator))
    context.cbr_url_el = context.browser.find_element(*locator)


@When('Нажали на ссылку "cbr.ru"')
def step(context):
    context.cbr_url_el.click()
    context.browser.switch_to.window(context.browser.window_handles[-1])


@Then('Проверили, что открыт сайт {url}')
def step(context, url):
    current_url = context.browser.current_url
    current_ps = context.browser.page_source
    context.browser.get("http://" + url)
    expected_ps = context.browser.page_source
    if current_ps != expected_ps:
        raise Exception(f"Неверный сайт, ожидалось:{url}, получено:{current_url}")


@When('Нажали на ссылку {text}')
def step(context, text):
    locator = (By.XPATH, f'//a[text()="{text}"]')
    wait(context.browser, 10).until(ec.element_to_be_clickable(locator))
    context.browser.find_element(*locator).click()


@When('Открыли раздел {text}')
def step(context, text):
    context.browser.find_element_by_xpath(f'//h2[text()="{text}"]').click()


@When('В поле Ваша благодарность ввели значение "{text}"')
def step(context, text):
    locator = (By.ID, 'MessageBody')
    wait(context.browser, 10).until(
        ec.presence_of_element_located(locator))
    context.browser.find_element(*locator).send_keys(text)


@When('Поставили галочку "Я согласен"')
def step(context):
    locator = (By.XPATH, '//*[@id="_agreementFlag"]')
    wait(context.browser, 10).until(
        ec.element_to_be_clickable(locator))
    context.browser.find_element(*locator).click()


@Then('Сделали скриншот')
def step(context):
    context.screenshots.append(context.browser.get_screenshot_as_png())


@When('Нажали на Три полоски')
def step(context):
    context.browser.find_element_by_xpath('//div[@id="layout"]//span[@class="burger"]').click()


@When('Нажали на раздел О сайте')
def step(context):
    locator = (By.XPATH, '//*[@id="page"]/div[5]/div/div[4]/div[1]/ul/li[20]/a')
    wait(context.browser, 10).until(ec.visibility_of_element_located(locator))
    el = context.browser.find_element(*locator)
    ActionChains(context.browser).move_to_element(el).perform()
    el.click()


@Then('Запомнили текст предупреждения')
def step(context):
    el = context.browser.find_element_by_xpath('//*[@id="content"]/p')
    context.warning_text = el.text


@When('Сменили язык страницы на en')
def step(context):
    locator = (By.XPATH, '//*[@id="layout"]/div[1]/div[2]/div/ul/li[2]/a')
    wait(context.browser, 10).until(ec.element_to_be_clickable(locator))
    context.browser.find_element(*locator).click()


@Then('Проверили, что текст отличается от запомненного текста ранее')
def step(context):
    current_warning_text = context.browser.find_element_by_xpath('//*[@id="content"]/p')
    if current_warning_text == context.warning_text:
        raise Exception('Текст предупреждения не отличается от запомненного текста ранее!')
