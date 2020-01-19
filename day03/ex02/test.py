import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ScrapBooker import ScrapBooker
import numpy as np

class ImageProcessor:

	def load(self, path):
		array = mpimg.imread(path)
		return (array)

	def display(self, array):
		img_plt = plt.imshow(array)
		plt.show()
		return (img_plt)

ip = ImageProcessor()
sb = ScrapBooker()

### test crop

#arr = ip.load("../resources/42AI.png")
#arr1 = sb.crop(arr, (100,100), (0,100))
#ip.display(arr1)


### test thin

# arr = np.array([[0,0,0,0,0],[0,1,1,1,1],[0,1,2,2,2], [0,1,2,3,3],[0,1,2,3,4]])
# print("Base array :\n", arr)

# arr1 = sb.thin(arr, 2, 0)
# print("vertical :\n", arr1)

# arr1 = sb.thin(arr, 2, 1)
# print("Horizontal :\n", arr1)

# arr1 = sb.thin(arr,  2, 0)
# arr1 = sb.thin(arr1, 2, 1)
# print("Both :\n", arr1)

### test juxtapose

#arr1 = np.concatenate((arr, arr), axis=0)
#print("test np.concat :\n", arr1)

# arr = ip.load("../resources/elon_weed.png")
# arr1 = sb.juxtapose(arr, 5, 1)
# ip.display(arr1)

### test mosaic

img = ip.load("../resources/elon_weed.png")
arr1 = sb.mosaic(img, (500, 500), 5)
print(type(arr1))
ip.display(arr1)

