# matrix-into-a-list-in-a-spiral

Реализована Python-библиотека, которая осуществляет получение квадратной матрицы (NxN) с удалённого сервера и возвращает её пользователю в виде List[int]. Список содержит результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла (см. test case ниже).

Пример исходной матрицы:

```
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
```

Матрица гарантированно содержит целые неотрицательные числа. Форматирование границ иными символами не предполагается.

## Выполнение и оформление

- Библиотека содержит функцию со следующим интерфейсом:

```python
async def get_matrix(url: str) -> List[int]:
    ...
```

- Функция единственным аргументом получает URL для загрузки матрицы с сервера по протоколу HTTP(S).

- Функция возвращает список, содержащий результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.

- Взаимодействие с сервером реализовано асинхронно - посредством aiohttp.

- Библиотека обрабатывает ошибки сервера и сетевые ошибки (Connection Timeout, Connection Refused, ...).

- Библиотека сохраняет свою работоспособность на квадратных матрицах другой размерности.

# [Реализация](https://github.com/Allswbr/matrix-into-a-list-in-a-spiral/blob/main/get_matrix/get_matrix.py)

# [Тестирование](https://github.com/Allswbr/matrix-into-a-list-in-a-spiral/blob/main/get_matrix/test.py)

## Примечание для пользователей ОС Windows:

Чтобы избежать ошибки __RuntimeError: Event loop is closed__, возникающей из-за различающихся циклов событий, перед вызовом функции __asyncio.run(get_matrix(URL))__ необходимо изменить политику цикла событий:

```python
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
