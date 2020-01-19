import numpy as np

class ScrapBooker:

	def crop(self, array, dim, pos=(0,0)):
		res = array[pos[1]: pos[1] + dim[1], pos[0]: pos[0] + dim[0], : ]
		if res.size:
			return(res)
		raise  ValueError("Bad values. The sum dimention  and position should be lower than the dimentions of the actual img")

	def thin(self, array, n, axis):
		if axis == 1:
			return(array[::n,::])
		elif axis == 0:
			return(array[::,::n])


	def juxtapose(self, array, n, axis):
		return (np.concatenate((array,) * n, axis=axis))

	def mosaic(self, array, dimensions, n = 4):
		res = ScrapBooker().juxtapose(array, n, axis=0)
		res = ScrapBooker().juxtapose(res, n, axis=1)
		return(res)
