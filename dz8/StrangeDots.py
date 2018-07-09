class Dots:
    def __init__(self, start, end):
        self.seg_start, self.seg_end = start, end

    def __getitem__(self, key):
        # a[key]
        if not isinstance(key, slice):
            subseg = (self.seg_end - self.seg_start) / (key-1)
            return [self.seg_start + subseg*i for i in range(0, key)]
        
        # a[i:n]; key == (start=i, stop=n, step=None)
        if not key.step:
            subseg = (self.seg_end - self.seg_start) / (key.stop-1)
            return self.seg_start + subseg*key.start
        
        # a[i:j:n]; key == (start=i, stop=j, step=n)
        start = 0        if not key.start else key.start 
        end   = key.step if not key.stop  else key.stop
        subseg = (self.seg_end - self.seg_start) / (key.step-1)
        return [self.seg_start + subseg*i for i in range(start, end)]