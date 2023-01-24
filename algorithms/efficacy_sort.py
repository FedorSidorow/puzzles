# id 79917026
class Intern:
    def __init__(self, name: str, points: int, penalty: int):
        self.name = name
        self.points = points
        self.penalty = penalty

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Intern):
            return(
                (-self.points, self.penalty, self.name) <
                (-other.points, other.penalty, other.name)
            )
        return NotImplemented


def quicksort(array: list):
    """Быстрая сортировка без дополнительной памяти.

    Сортирует массив на месте. Для работы необходим определенный метод __lt__.

    Args:
        array (list): массив для сортировки
    """
    def _quicksort(low: int, high: int) -> None:
        if low >= high:
            return
        left = low
        right = high
        pivot = array[(right + left) // 2]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left < right:
                array[left], array[right] = array[right], array[left]
            if left <= right:
                left += 1
                right -= 1
        _quicksort(low, right)
        _quicksort(left, high)

    _quicksort(0, len(array) - 1)


if __name__ == '__main__':
    number = int(input())
    interns = []
    for index in range(number):
        name, points, penalty = input().split()
        interns.append(
            Intern(points=int(points), penalty=int(penalty), name=name)
        )
    quicksort(interns)
    print(*interns, sep='\n')
