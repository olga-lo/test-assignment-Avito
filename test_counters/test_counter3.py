import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)  # Установим headless=False, чтобы видеть процесс
       yield browser
       browser.close()


def test_case_3(browser):
   # Открыть страницу счетчиков
   page = browser.new_page()
   page.goto("https://www.avito.ru/avito-care/eco-impact", timeout=60000)  # Установить таймаут в 60 секунд


   # Проверить существование папки "output" и создать её, если она не существует
   output_dir = "output"
   if not os.path.exists(output_dir):
       os.makedirs(output_dir)


   # Найти все элементы с классом ".desktop-impact-item-eeQO3"
   counters = page.query_selector_all(".desktop-impact-item-eeQO3")


   print(f"Всего счетчиков найдено: {len(counters)}")  # Вывести количество найденных счетчиков


   # Проверить, есть ли шестой счетчик электроэнергии
   if len(counters) >= 6:
       target_counter = counters[5]  # Шестой счетчик электроэнергии


       # Сделать скриншот счетчика и сохранить его в папку "output"
       screenshot_path = os.path.join(output_dir, "test_case_3.png")
       target_counter.screenshot(path=screenshot_path)


       print(f"Сохраняем скриншот в: {screenshot_path}")
       print("Скриншот сохранен успешно")
   else:
       print("Шестой счетчик электроэнергии не найден.")


   # Закрыть страницу
   page.close()
