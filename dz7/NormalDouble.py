class Normal:
    def __init__(self, start):
        self.val = start

    def what(self):
        return self.val

    def swap(self, other):
        self.val, other.val = other.val, self.val

class Double:
    def __init__(self, start):
        self.val = start*2

    def what(self):
        return self.val*2

    def swap(self, other):
        self.val, other.val = other.val*2, self.val*2