# ID 78826269
from typing import List, Tuple


MAX_NUM = 1000000000


def read_data() -> Tuple[int, List[int]]:
    """Чтение данных.

    Returns:
        Tuple[int, List[int]]: Возвращает кортеж из количества
        участков и их расположения.
    """
    num_house: int = int(input())
    data: List[int] = list(map(int, input().split()))
    return num_house, data


def find_nearest(num_house: int, data: List[int]) -> List[int]:
    """Находит растояния для всех участков до ближайшего нуля.

    Args:
        num_house (int): Количество участков.
        data (List[int]): Расположение участков.

    Returns:
        List[int]: Растояние до ближайшего пустыря.
    """
    distance: List[int] = list(range(num_house))
    num_house -= 1
    count: int = MAX_NUM
    for position, house in enumerate(data):
        if house == 0:
            count = 0
        else:
            count += 1
        distance[position] = count
    for position, house in enumerate(data[::-1]):
        if house == 0:
            count = 0
        else:
            count += 1
        if distance[num_house - position] > count:
            distance[num_house - position] = count
    return distance


def main():
    """Для каждого из участков выводит расстояние до ближайшего нуля."""
    num_house, data = read_data()
    distance = find_nearest(num_house, data)
    print(*distance)


if __name__ == '__main__':
    main()
