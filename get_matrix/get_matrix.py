import aiohttp
from typing import List, Tuple, Any
import math


def filter_function(char: str) -> bool:
    if char.isdigit() or char == ' ':
        return True
    return False


def snail(m: List[Tuple[Any, ...]]) -> List[int]:
    return list(m[0])+snail(list(zip(*m[1:]))[::-1]) if m else []


async def get_matrix(url: str) -> List[int]:
    """
    Функция получает URL адрес сервера, на котором находится матрица для обработки.
    Полученные данные очищаются от некорректных символов и затем преобразуются в список, содержащий только числа.
    Размер матрицы - n.
    Список преобразуется в матрицу и транспонируется.
    С помощью вспомогательной функции производится обход по спирали и вовзвращается результат.
    :param url: URL для загрузки матрицы с сервера по протоколу HTTP(S)
    :return: список, содержащий результат обхода полученной матрицы
     по спирали: против часовой стрелки, начиная с левого верхнего угла
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, timeout=1) as response:
                digits: List[str] = ''.join(filter(filter_function, await response.text())).split()
                n: int = int(math.sqrt(len(digits)))
                matrix: List[List[int]] = [list(map(int, digits[i * n:(i + 1) * n])) for i in range(n)]
                transpose_matrix: List[Tuple[Any, ...]] = list(list(zip(*matrix)))
    except aiohttp.ServerTimeoutError as e:
        print("Timeout error: {}".format(e))
        exit()
    except aiohttp.ClientResponseError as e:
        print("Client response error: {}".format(e))
        exit()
    except aiohttp.InvalidURL as e:
        print("Invalid URL: {}".format(e))
        exit()
    except aiohttp.ClientConnectionError as e:
        print("Client connection error: {}".format(e))
        exit()
    except aiohttp.ClientPayloadError as e:
        print("Client payload error: {}".format(e))
        exit()
    except aiohttp.ClientError as e:
        print("Client Error: {}".format(e))
        exit()
    except Exception as e:
        print("Exception: {}".format(e))
        exit()
    return snail(transpose_matrix)
