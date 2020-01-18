from csvreader import CsvReader
import csv


if __name__ == "__main__":
	with CsvReader('good.csv') as file:
		data = file.getdata()
		header = file.getheader()
		
		[print(d) for d in data]
		print("\n\n")
		print(header)

	with CsvReader('bad.csv') as file:
		if file == None:
			print("It work ! File is corrupted !")
		else :
			print("program don't work")


