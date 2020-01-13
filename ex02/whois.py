import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
    if n != 0:
    	print ("I'm Even.") if n % 2 == 0 else print ("I'm odd.")
    else:
    	print ("I'm Zero.")
else:
    print ("ERROR")
