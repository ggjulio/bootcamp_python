import csv

class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file_obj = open(self.filename, "r")

	def __enter__(self):
		return (self.file_obj)

	def getdata(self):
		data = csv.reader(self.file_obj, delimiter=self.sep, has_header=self.header)
		data = data[self.skip_top: data.count('\n') - self.skip_bottom]
		return (data)

	def getheader(self):
		pass

	def __exit__(self, type, value, traceback):
		if self.file_obj:
			self.file_obj.close()
	
