import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from ColorFilter import ColorFilter

class ImageProcessor:

	def load(self, path):
		array = mpimg.imread(path)
		return (array)

	def display(self, array):
		img_plt = plt.imshow(array)
		plt.show()
		return (img_plt)

cf = ColorFilter()
ip = ImageProcessor()

arr = ip.load("../resources/elon_weed.png")
ip.display(cf.invert(arr))

arr = ip.load("../resources/elon_weed.png")
ip.display(cf.to_red(arr))

arr = ip.load("../resources/elon_weed.png")
ip.display(cf.to_green(arr))

arr = ip.load("../resources/elon_weed.png")
ip.display(cf.to_blue(arr))

