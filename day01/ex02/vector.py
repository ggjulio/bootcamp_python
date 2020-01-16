class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = len(self.vector)

    def __add__(self, x):
        return(Vector([v + x for v in self.vector]))

    def __radd__(self, x):
        return(Vector([v + x for v in self.vector]))

    def __sub__(self, x):
        return(Vector([v - x for v in self.vector]))

    def __rsub__(self, x):
        return(Vector([v - x for v in self.vector]))

    def __truediv__(self, x):
        return(Vector([v / x for v in self.vector]))

    def __rtruediv__(self, x):
        return(Vector([v / x for v in self.vector]))

    def __mul__(self, x):
        return(Vector([v * x for v in self.vector]))

    def __rmul__(self, x):
        return(Vector([v * x for v in self.vector]))

    def __repr__(self):
        return (self.vector.__repr__())