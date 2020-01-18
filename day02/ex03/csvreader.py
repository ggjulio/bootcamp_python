import csv

class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.data_header = None
		self.data = []
		self.file_obj = None

	def __enter__(self):
		try:
			self.file_obj = open(self.filename, "r")
			csv_reader = csv.reader(self.file_obj, delimiter=self.sep)
			if not self.header: 
				self.data_header = next(csv_reader)
			for l in csv_reader:
				self.data.append(l)
			if not self.header and all([ len(l) == len(self.data_header) for l in self.data]):
				return (self)
		except FileNotFoundError:
			pass	
		return (None)

	def getdata(self):
		return (self.data)

	def getheader(self):
		return(self.data_header)

	def __exit__(self, type, value, traceback):
		if self.file_obj:
			self.file_obj.close()
	
