import string
import sys

def text_analyzer(text = None):
	""" 
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
    	"""
	if text is None:
		text = input("What is the next to analyze ?\n>> ");
	print ("The text contains %d characters :" % len(text))
	print ("- %d upper letters" % sum(1 for c in text if c.isupper()))
	print ("- %d lower letters" % sum(1 for c in text if c.islower()))
	print ("- %d punctuation marks" % sum([1 for c in text if c in string.punctuation]))
	print ("- %d spaces" % sum(1 for c in text if c.isspace()))
