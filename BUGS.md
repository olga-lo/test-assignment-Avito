Привет всем, кто заглянул сюда!<br>
Здесь представлено решение 1 части тестового задания от Avito [Ссылка на тестовое задание](https://drive.google.com/file/d/1agx-6btmmj33I76wF3Chqkow5Mlic2oK/view?usp=sharing)   
Если задание по ссылке недоступно, вы можете посмотреть скрины задания в папке [test_conditions](https://github.com/olga-lo/test-assignment-Avito/tree/main/test_conditions)  


Выполняя это тестовое задание, я обнаружила 2 бага на настоящем сайте Avito.ru 🙂  
В этом файле они под номерами **20 и 21**  
Баги зафиксированы и переданы в службу поддержки.  
Обнаружены 3 июня 2024 года.  
По состоянию на 11 июня 2024 года баги всё ещё присутствуют на реальном сайте Avito.


## Задание 1. Перечислите все имеющиеся баги на странице поиска. Укажите их приоритет (high, medium, low)

## Баги на странице поиска

### 1. Лого компании на странице поиска написан неверно
**Приоритет: High** (Так как лого - это визитная карточка компании, если он указано неверно у пользователя может сложиться впечатление, что он находится не на настоящей странице компании).
![Скрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/1.1.jpg)


### 2. Хлебные крошки на странице поиска написаны с маленькой буквы
**Приоритет: Low** (Баг UI-дизайна, на работу страницы не влияет, исправить можно в последнюю очередь). 
![Скрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/2.jpg)



### 3. Отображение результатов на странице не соответствует выбранному значку вида отображения “Карта”
**Приоритет: Medium** (Баг не блокирует главную функцию сайта, поиск осуществляется, результаты видны, но это вводит в заблуждение, нарушается ожидаемое поведение сайта, пользователь может быть недоволен).
![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/3.jpg)



### 4. Интервал между названием и изображением в первой карточке слева отличается от интервала в остальных карточках
**Приоритет: Low** (Баг UI-дизайна, на функциональность не влияет, основной контент читаемый).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/4.jpg)


### 5. Размер шрифта в средней карточке во втором ряду отличается от размера шрифта в остальных карточках
**Приоритет: Low** (Баг UI-дизайна, на функциональность не влияет, основной контент читаемый).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/5.jpg)


### 6. Введенный текст в поле “Производитель” отображается серым цветом как цвет плейсхолдера
**Приоритет: Medium** (Баг не блокирует функцию сайта, ввод осуществляется, но это может запутать пользователя, он может подумать, что текст не введен или не принят, фильтром перестанут пользоваться).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/6.jpg)


### 7. Отсутствие кнопки “Сбросить” у выбранного фильтра “Память”
**Приоритет: Medium** (Относится к дефекту UX-дизайна. Баг не блокирует фильтр, выбор осуществляется, но это не удобно для пользователя: он не видит визуально возможности отказаться от выбранного фильтра. Пользователь ожидает кнопку сброса рядом. Не все могут догадаться, что, для снятия выбора нужно заново нажать выбранный элемент, а вариант обновить страницу, чтобы сбросить фильтр, принесет негативный эффект и увеличит время поиска).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/7.jpg)


### 8. Отсутствие кнопки “Сбросить” у выбранного фильтра “Цвет”
**Приоритет: Medium** (То же самое как с фильтром “Память”).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/8.jpg)


### 9. Вариант “белый” в фильтре “Цвет” при невыбранном состоянии выделен черной рамкой
**Приоритет: Low** (Баг визуальный, не блокирует работу фильтра, но путает пользователя в том, какой цвет он выбрал. Если подтвердиться, что, баг влияет на выбор пользователей лучше поменять приоритет на Medium).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/9.jpg)


### 10. Кнопка “Какое состояние выбрать” в фильтре “Состояние” не выровнена относительно левого края
**Приоритет: Low** (Баг визуальный, относится к дефекту UI-дизайна, не блокирует работу фильтра).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/10.jpg)


### 11. Отсутствие указания валюты в фильтре “Цена”
**Приоритет: Medium** (Пользователь может не понимать, в какой валюте выставлены цены, это может повлиять на восприятие цены, решение о покупке).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/11.jpg)


### 12. Отсутствие кнопки-крестика для очистки в поле “Цена до” фильтра “Цена” при введенном значении
**Приоритет: Medium** (То же самое как с фильтром “Память”).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/12.jpg)


### 13. Поля “Цена от” и “Цена до” имеют разную длину
**Приоритет: Low** (Баг визуальный, относится к дефекту UI-дизайна, не блокирует работу фильтра).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/13.jpg)


### 14. Нет названия у фильтра “Вид компании”
**Приоритет: Low** (Пользователи могу не понять назначение фильтра без названия, а это значит, что пользователю будет трудно отфильтровать и найти нужную информацию. Название фильтра ускоряет его выбор пользователем. А также у всех фильтров есть название, а значит нужно оформить страницу в едином стиле).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/14.jpg)


### 15. Нет названия у группы чек-боксов с выбором варианта доставки
**Приоритет: Low** (То же самое как с п.14).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/15.jpg)


### 16. Плейсхолдер “Что-то важное для вас” в поле “Слова в описании” и имеет разный отступ относительно других плейсхолдеров на странице
**Приоритет: Low** (Баг визуальный, относится к дефекту UI-дизайна).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/16.jpg)


### 17. Названия и параметры фильтров на странице поиска выполнены в сером цвете
**Приоритет: Medium** (Серый цвет элементов может путать пользователей, так как ассоциируется с неактивными или отключенными элементами интерфейса. И если активные элементы окрашены в серый цвет, пользователи могут подумать, что они не могут взаимодействовать с этими элементами).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/17.1.jpg)
![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/17.2.jpg)


### 18. Выбранный фильтр по городу "Москва" не отображается в средней карточке из второго ряда 
**Приоритет: High**: (Фильтрация по городу является ключевой функциональностью для пользователей или бизнеса, и отсутствие этой функции сильно влияет на пользовательский опыт. Нарушается ожидаемое поведение сайта, может привести к недовольству пользователя).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/18.jpg)


### 19. Отсутствует переключатель у фильтра "Сначала из Москвы"
**Приоритет: Medium**: (Не критично нарушает функциональность, но ухудшает удобство использования и может привести к недовольству пользователей, особенно тех, кто хочет видеть товары именно из Москвы в первую очередь).

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/19.jpg)


Ниже представлены баги, найденные на реальном сайте Avito:

### 20. В фильтре "Цена" на странице поиска названия полей "От" и "до" написаны разным регистром  
**Приоритет: Low**  
**Описание:**  На мой взгляд, когда пользователи видят поля, написанными в разном регистре, это может создать впечатление непрофессиональности. Здесь не соблюдены стандарты оформления, это может вызывать у пользователей недоверие. Даже такие мелочи в дизайне могут повлиять на их общее восприятие сайта. 
Также разные регистры могут сбивать с толку и затруднять восприятие информации.

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/20.jpg)



### 21. Чек-бокс "Смартфон проверен" в группе чек-боксов "Дополнительно" отделен большим интервалом, чем остальные чек-боксы в этой группе 
**Приоритет: Low**  
**Описание:** Когда один чек-бокс отличается по интервалу, это создает визуальный диссонанс и может выглядеть как ошибка. Визуальная несогласованность может затруднить восприятие информации и использование интерфейса. Правильное выравнивание и интервалы помогают пользователям быстро и легко воспринимать информацию.

![Cкрин](https://github.com/olga-lo/test-assignment-Avito/blob/main/images/21.jpg)

















