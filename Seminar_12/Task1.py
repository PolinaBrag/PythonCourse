# класс-функция
from collections import deque


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
            self.memory.append({n: result})
        return result

    def view(self):
        return self.memory


if __name__ == '__main__':
    f = Factorial(3)
    print(f(5))
    print(f(2))
    print(f(12))
    print(f(7))
    print(f(21))
    print(f.view())