#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from behave import *
from features.pages import *


@Given('Зашли на сайт "google.ru"')
def step(context):
    context.page = GoogleMainPage(context)
    context.page.visit()


@Then('Проверили, что появилось поле "Поиск"')
def step(context):
    assert context.page.search_input


@When('Ввели в поле Поиск значение "{text}"')
def step(context, text):
    context.page.search_input.send_keys(text)


@When('Нажали на кнопку "Поиск в Google"')
def step(context):
    context.page.search_button.click()
    context.page = GoogleSearchPage(context)


@Then('Нашли ссылку "cbr.ru"')
def step(context):
    assert context.page.link_cbr_ru


@When('Нажали на ссылку "cbr.ru"')
def step(context):
    context.page.link_cbr_ru.click()
    context.page.go_to_last_page()
    context.page = CbrMainPage(context)


@Then('Проверили, что открыт сайт {url}')
def step(context, url):
    context.page.assert_page(url)


@When('Нажали на ссылку Интернет-приемная')
def step(context):
    context.page.reception_button.click()
    context.page = CbrReceptionPage(context)


@When('Открыли раздел Написать благодарность')
def step(context):
    context.page.gratitude_button.click()
    context.page = CbrGratitudePage(context)


@When('В поле Ваша благодарность ввели значение "{text}"')
def step(context, text):
    context.page.message_input.send_keys(text)


@When('Поставили галочку "Я согласен"')
def step(context):
    context.page.agreement_flag.click()


@Then('Сделали скриншот')
def step(context):
    context.page.screenshot(context)


@When('Нажали на Три полоски')
def step(context):
    context.page.burger_button.click()


@When('Нажали на раздел О сайте')
def step(context):
    context.page.about.click()


@When('Нажали на ссылку Предупреждение')
def step(context):
    context.page.warning_link.click()
    context.page = CbrWarningPage(context)


@Then('Запомнили текст предупреждения')
def step(context):
    context.warning_text = context.page.warning.text


@When('Сменили язык страницы на en')
def step(context):
    context.page.en.click()


@Then('Проверили, что текст отличается от запомненного текста ранее')
def step(context):
    assert context.warning_text != context.page.warning.text
