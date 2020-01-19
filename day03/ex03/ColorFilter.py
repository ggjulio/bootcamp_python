
class ColorFilter:

	@staticmethod
	def invert(array):
		return (1 - array)

	@staticmethod
	def to_blue(array):
		arr = array[:]
		arr[:,:,0] = 0
		arr[:,:,1] = 0
		return (arr)

	@staticmethod
	def to_green(array):
		arr = array[:]
		arr[:,:,0] = 0
		arr[:,:,2] = 0
		return (arr)

	@staticmethod
	def to_red(array):
		arr = array[:]
		arr[:,:,1] = 0
		arr[:,:,2] = 0
		return (arr)

	@staticmethod
	def celluloid(array):
		pass

	@staticmethod
	def to_grayscale(array, filter):
		pass



