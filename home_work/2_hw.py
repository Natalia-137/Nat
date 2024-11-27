def task_1(a: int = 3, b: float = 2.5, c: str = 'ligo', d: list = [1, 3, 7], e: bool = False) -> str:

    return type(a), type(b), type(c), type(d), type(e)

print(task_1())


def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]
print(task_2())
#числа Фибоначчи


def task_3 (a: float) -> float:
    return a ** 2

print(task_3(1.2))
