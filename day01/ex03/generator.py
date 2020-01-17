import string
import random as rd


def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	lst = text.split(sep)
	if option == "shuffle":
		rd.shuffle(lst)
	elif option == "unique":
		lst = list(set(lst))
	elif option == "ordered":
		lst.sort()
	elif option:
		print("shit")
		raise ValueError("Option can be : 'shuffle', 'unique', 'ordered'")

	for w in lst:
		yield w
