# id 79308537


from operator import add, floordiv, mul, sub


class Stack:
    """Стек на списке.

    Тип LIFO.
    """
    def __init__(self):
        self.__items = []

    def push(self, item: any):
        """Поместить объект в стек.

        Args:
            item (any): Объект для хранения.
        """
        self.__items.append(item)

    def pop(self) -> any:
        """Вернуть объект из стека.

        Returns:
            any: Объект из стека.
        """
        return self.__items.pop()


def calc(data: str) -> int:
    """Подсчет арифмитического выражения.

    Выражение записано в обратной польской нотации.

    Args:
        data (str): Выражение для подсчета.

    Returns:
        int: Результат арифмитического выражения.
    """
    stack = Stack()
    num1: int = 0
    num2: int = 0
    operator = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": floordiv
    }
    for word in data.split():
        try:
            stack.push(int(word))
        except ValueError:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.push(operator[word](num1, num2))
    return stack.pop()


def main():
    """Подсчет арифмитического выражения.
    """
    print(calc(input()))


if __name__ == '__main__':
    main()
