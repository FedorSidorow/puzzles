# id 79309295
from typing import List


class MyDeque:
    """Очередь на кольцевом буфере.
    """
    def __init__(self, max_size: int):
        self.__queue: List = [None] * max_size
        self.__max_n: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def push_front(self, value: any):
        """Поместить элемент в начало очереди.

        Args:
            value (any): объект который нужно поместить в очередь.

        Raises:
            MemoryError: Попытка поместить объект в полную очередь.
        """
        if self.__size == self.__max_n:
            raise MemoryError("Deck is full")
        self.__queue[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_n
        self.__size += 1

    def push_back(self, value: any):
        """Поместить элемент в конец очереди.

        Args:
            value (any): объект который нужно поместить в очередь.

        Raises:
            MemoryError: Попытка поместить объект в полную очередь.
        """
        if self.__size == self.__max_n:
            raise MemoryError("Deck is full")
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def pop_front(self) -> any:
        """Вернуть объект из начала очереди.

        Raises:
            ValueError: Попытка получить объект из пустой очереди.

        Returns:
            any: объект из очереди.
        """
        if self.__size == 0:
            raise ValueError("Deck is empty")
        pop_value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return pop_value

    def pop_back(self) -> any:
        """Вернуть объект с конца очереди.

        Raises:
            ValueError: Попытка получить объект из пустой очереди.

        Returns:
            any: объект из очереди.
        """
        if self.__size == 0:
            raise ValueError("Deck is empty")
        pop_value = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_n
        self.__size -= 1
        return pop_value


def main():
    count_command = int(input())
    queue_size = int(input())
    instance = MyDeque(queue_size)
    for _ in range(count_command):
        command, *args = input().split()
        try:
            res = getattr(instance, command)(*args)
            if res:
                print(res)
        except (MemoryError, ValueError):
            print("error")


if __name__ == '__main__':
    main()
