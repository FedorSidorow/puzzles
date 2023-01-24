# ID 78825226
from typing import Dict, Tuple


def read_data() -> Tuple[int, str]:
    """Чтение данных.
    Считывает количество пальцев у игроков
    (сколько смогут нажать в один момент времени) и игровое поле 4*4.

    Returns:
        Tuple[int, str]: Количество пальцев и игровое поле.
    """
    keys: int = int(input())
    data: str = ""
    for _ in range(4):
        data += input()
    return keys, data


def get_score(keys: int, data: str) -> int:
    """Подсчет количества очков с учетом возможностей игроков.

    Args:
        keys (int): Количество пальцев на руках у одного игрока.
        data (str): Игровое поле 4*4

    Returns:
        int: Количество полученных очков.
    """
    keys += keys
    count: Dict[str, int] = {str(x): 0 for x in range(10)}
    count["."] = 0
    score: int = 0
    for char in data:
        count[char] += 1
    for i in "0123456789":
        if 0 < count[i] <= keys:
            score += 1
    return score


def main():
    """Игра ловкость рук.
    В момент времени t игрок должен одновременно нажать на все клавиши,
    на которых написана цифра t.
    Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
    Если в момент времени t нажаты все нужные клавиши,
    то игроки получают 1 балл.
    """
    keys, data = read_data()
    score = get_score(keys, data)
    print(score)


if __name__ == '__main__':
    main()
