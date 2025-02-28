from collections import deque


class Factorial:
    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwds):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return self.memory[-1]

    def old(self):
        return self.memory


if __name__ == '__main__':
    f = Factorial(2)
    for i in range(10):
        print(f(i))
        print(f.old())
