class Unary:
    def __init__(self, str):
        self.value = "|" * len(str)
        self.idx = 0

    def __str__(self):
        return self.value

    def __bool__(self):
        return bool(self.value)

    def __len__(self):
        return len(self.value)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.value[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return Unary(item)

    def __ior__(self, other):
        self.value += other.value
        return self

    def __invert__(self):
        self.value = "|" * (len(self.value) // 2)
        return self

    def __pos__(self):
        self.value += "|"
        return self