import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:

	def load(self, path):
		array = mpimg.imread(path)
		return (array)

	def display(self, array):
		img_plt = plt.imshow(array)
		plt.show()
		return (img_plt)
		
		
