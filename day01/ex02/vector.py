class Vector:
	def __init__(self, vector):
		if type(vector) == int:
			self.vector = list(range(0, vector))
		elif type(vector) == tuple:
			self.vector = list(range(vector[0], vector[1]))
		else:
			self.vector = vector
		self.size = len(self.vector)

	def __add__(self, x):
		return(Vector([v + x for v in self.vector]))

	def __radd__(self, x):
		return(Vector([v + x for v in self.vector]))

	def __sub__(self, x):
		return(Vector([v - x for v in self.vector]))

	def __rsub__(self, x):
		return(Vector([x - v for v in self.vector]))

	def __truediv__(self, x):
		try:
			return(Vector([v / x for v in self.vector]))
		except ZeroDivisionError as e:
			return(e)

	def __rtruediv__(self, x):
		try:
			return(Vector([x / v for v in self.vector]))
		except ZeroDivisionError as e:
			return(e)

	def __mul__(self, x):
		return(Vector([v * x for v in self.vector]))

	def __rmul__(self, x):
		return(Vector([v * x for v in self.vector]))

	def __repr__(self):
		return (self.vector.__repr__())