import pandas as pd

class FileLoader:

	@staticmethod
	def load(path):
		data = pd.read_csv(path)
		print(f"Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}")
		return (data)

	@staticmethod
	def display(dataframe, n):
		if n < 0:
			return (dataframe.tail(-n))
		else:
			return (dataframe.head(n))