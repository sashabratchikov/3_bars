# Ближайшие бары

`bars.py` содержит 3 функции для расчетов:

`get_biggest_bar` – принимает список баров и возвращает название бара, с наибольшим количеством мест
`get_smallest_bar` – принимает список баров и возвращает название бара, с наименьшим количеством мест
`get_closest_bar` – принимает список баров, долготу и широту и возвращает бар, ближайший к данным координатам

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py ../data/bars.json # possibly requires call of python3 executive instead of just python

```
Спросит координаты:
```bash

Please input your latitude: 37.5
Please input your longitude: 66.1

```
И выдаст результат:
```bash

Biggest bar:  Спорт бар «Красная машина»
Smallest bar:  БАР. СОКИ
Closest bar:  Таверна

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
