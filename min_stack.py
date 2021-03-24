from collections import deque


class MinStack:
    def __init__(self):
        self.s = deque()
        self.min = None

    def push(self, x):
        if not self.s:
            self.s.append(x)
            self.min = x
        elif x > self.min:
            self.s.append(x)
        else:
            self.s.append(2*x-self.min)
            self.min = x

    def pop(self):
        if not self.s:
            raise("Stack underflow!")
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()

    def minimum(self):
        return self.min

if __name__ == "__main__":
    s = MinStack()
    s.push(6)
    assert s.minimum() == 6

    s.push(7)
    assert s.minimum() == 6

    s.push(5)
    assert s.minimum() == 5

    s.push(3)
    assert s.minimum() == 3

    s.pop()
    assert s.minimum() == 5

    s.pop()
    assert s.minimum() == 6
