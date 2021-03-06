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
		lst.sort(key=str.swapcase)
	elif option:
		raise ValueError("Option can be : 'shuffle', 'unique', 'ordered'")

	[(yield w) for w in lst]
