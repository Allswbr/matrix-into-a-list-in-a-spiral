from get_matrix import get_matrix
from typing import List
import asyncio
import os

# RuntimeError: Event loop is closed
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

SOURCE_URL: List[str] = [
    "https://raw.githubusercontent.com/Allswbr/matrix-into-a-list-in-a-spiral/main/test.txt",
    "https://raw.githubusercontent.com/Allswbr/matrix-into-a-list-in-a-spiral/main/test1.txt",
    "https://raw.githubusercontent.com/Allswbr/matrix-into-a-list-in-a-spiral/main/test2.txt",
    "https://raw.githubusercontent.com/Allswbr/matrix-into-a-list-in-a-spiral/main/test3.txt",
    "https://raw.githubusercontent.com/Allswbr/matrix-into-a-list-in-a-spiral/main/test4.txt"]

TRAVERSAL: List[List[int]] = \
    [[10, 50, 90, 130,
      140, 150, 160, 120,
      80, 40, 30, 20,
      60, 100, 110, 70, ],
     [10, 50,
      60, 20, ],
     [10, 50, 90,
      100, 110, 70,
      30, 20, 60, ],
     [10, ],
     [10, 70, 130, 190, 250, 310,
      320, 330, 340, 350, 360, 300,
      240, 180, 120, 60, 50, 40,
      30, 20, 80, 140, 200, 260,
      270, 280, 290, 230, 170, 110,
      100, 90, 150, 210, 220, 160]]


def test_get_matrix():
    for i in range(5):
        assert asyncio.run(get_matrix(SOURCE_URL[i])) == TRAVERSAL[i]


test_get_matrix()
