# test-assignment-Avito

## Понятная инструкця как воспроизвести авто-тесты

Чтобы установить необходимые инструменты для автотестов понадобится Терминал

### Как открыть Терминал на компьютере:
**Windows:**
1. Нажмите клавиши Win + R, чтобы открыть диалог "Выполнить".
2. Введите cmd и нажмите Enter.
   
**macOS:**
1. Откройте Finder.
2. Перейдите в Приложения -> Служебные программы.
3. Запустите Терминал.
   
**Linux:**
1. Нажмите клавиши Ctrl + Alt + T
   
### Как установить и настроить необходимые инструменты для автотестов:
Запускайте команды через Терминал по порядку:  

**1. Установить Playwright:**

Авто-тест запускается в браузере Playwright. Это инструмент для автоматизации браузерного тестирования. 
```
pip install playwright
```

**2. Установить Chromium-драйвер:**

Для использования Playwright в связке с браузером Chromium потребуется соответствующий драйвер.<br> Команда установит Chromium и другие браузеры, которые могут быть использованы с Playwright.
  
```
python -m playwright install
```

**3. Установите Pytest, если он еще не установлен:**

```
pip install pytest
```
**4. Скачайте PyCharm Community Edition**

[Ссылка на официальный сайт jetbrains.com](URLhttps://www.jetbrains.com/ru-ru/pycharm/download/?section=windows)

### Как запустить автотетсы

Для запуска авто-тестов можно использовать Терминал, PyCharm или любую другую IDE <br>
Ниже представлен вариант запуска автотестов в PyCharm

**1. Откройте PyCharm, создайте и назовите новый проект:**

File > New Project > Autotests

**2. Создайте в проекте файл с типом файла ".py":**

 New > File > PythonFile > test_counters.py

**3. Скоприруйте код ниже и вставьте в файл test_counters.py:**

**Авто-тест 1:**

```
import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)  # Установим headless=False, чтобы видеть процесс
       yield browser
       browser.close()


def test_case_1(browser):
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


   # Проверить, есть ли второй счетчик CO2
   if len(counters) >= 2:
       target_counter = counters[1]  # Второй счетчик CO2


       # Сделать скриншот счетчика и сохранить его в папку "output"
       screenshot_path = os.path.join(output_dir, "test_case_1.png")
       target_counter.screenshot(path=screenshot_path)


       print(f"Сохраняем скриншот в: {screenshot_path}")
       print("Скриншот сохранен успешно")
   else:
       print("Второй счетчик CO2 не найден.")


   # Закрыть страницу
   page.close()
```

**4. Запустите авто-тест одним из вариантов:**

- с помощью команды Run
- в терминале PyCharm перейдите в нужную директорию с помощью команды:
  
```
cd
```

и запустите команду pytest
  
```
pytest test_counters.py
```

**5. Проверьте наличие скриншота test_case_1.png в папке "output" на своем локальном комьютере**

**6. Скоприруйте код ниже, вставьте в файл test_counters.py и запустите авто-тест:**

**Авто-тест 2:**

```
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

```

**6. Проверьте наличие скриншота test_case_2.png в папке "output" на своем локальном комьютере**

**7. Скоприруйте код ниже, вставьте в файл test_counters.py и запустите авто-тест:**

**Авто-тест 3:**

```
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

```

**7. Проверьте наличие скриншота test_case_3.png в папке "output" на своем локальном комьютере**
