import sys

if len(sys.argv) != 2:
    sys.exit("ERROR")
try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit("ERROR")
if n != 0:
    print ("I'm Even.") if n % 2 == 0 else print ("I'm odd.")
else:
    print ("I'm Zero.")
