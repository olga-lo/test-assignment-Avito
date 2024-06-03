import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)  # Открытие браузера в режиме без headless для визуального контроля
       yield browser
       browser.close()


def test_case_2(browser):
   # Открыть страницу счетчиков
   page = browser.new_page()
   page.goto("https://www.avito.ru/avito-care/eco-impact", timeout=60000)  # Установить таймаут в 60 секунд


   # Проверить существование папки "output" и создать её, если она не существует
   output_dir = "output"
   if not os.path.exists(output_dir):
       os.makedirs(output_dir)


   # Найти все счетчики на странице
   counters = page.query_selector_all(".desktop-impact-item-eeQO3")


   print(f"Всего счетчиков найдено: {len(counters)}")
   # Проверить, есть ли четвертый счетчик
   if len(counters) >= 4:
       target_counter = counters[3]  # Четвертый счетчик (второй ряд, первый по счету - вода)


       # Сделать скриншот счетчика и сохранить его в папку "output"
       screenshot_path = os.path.join(output_dir, "test_case_2.png")
       print(f"Сохраняем скриншот в: {screenshot_path}")
       target_counter.screenshot(path=screenshot_path)
       print(f"Скриншот сохранен успешно")
   else:
       print("Четвертый счетчик не найден")


   # Закрыть страницу
   page.close()
