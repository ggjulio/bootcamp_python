import sys

if len(sys.argv) > 1:
	lst = sys.argv[1:]
	str = "".join(lst)[::-1]
	str = str.swapcase()
	print (str)

