from math import sqrt

message: str = 'Добро пожаловать в самую лучшую программу для вычисления '\
               'квадратного корня из заданного числа'
root: float = 0.0


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Возращает корень или 0."""
    if your_number <= 0:
        return 0
    global root
    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')
    return root


print(message)
calc(25.5)
