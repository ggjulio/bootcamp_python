import sys

def show_usage():
	sys.exit("Usage: python operations.py \nExample:\n	python operations.py 10 3")

def do_sum(x, y):
	print ("Sum : %15.d" % (x + y))

def do_difference(x, y):
	print ("Difference : %8.d" % (x - y))

def do_product(x, y):
	print ("Product : %11.d" % (x * y))

def do_quotient(x, y):
	print ("Quotient :     ", end='')
	try:
		print (x / y)
	except ZeroDivisionError:
            print ("ERROR (div by zero)")

def do_reminder(x, y):
	print ("Reminder :     ", end='')
	try:
		print (x % y)
	except ZeroDivisionError:
            print ("ERROR (modulo by zero)")

ac = len(sys.argv)
if ac != 3:
	if ac > 3:
		print ("InputError: too many arguments\n")
	sys.exit(show_usage())
try:
	x, y = int(sys.argv[1]), int(sys.argv[2])
except ValueError:
	print ("InputError: Only number\n")
	sys.exit(show_usage())

do_sum(x, y)
do_difference(x, y)
do_product(x, y)
do_quotient(x, y)
do_reminder(x, y)

# ZeroDivisionError
# NameError
# TypeError

#except TypeError:
