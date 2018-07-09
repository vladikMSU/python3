class Delay:
    def __init__(self, init_val):
        self.slot = init_val

    def delay(self, new):
        ret_val, self.slot = self.slot, new
        return ret_val