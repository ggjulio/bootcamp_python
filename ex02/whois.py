import sys

if len(sys.argv) == 2:
    print ("EVEN") if int(sys.argv[1]) % 2 == 0 else print ("ODD")
else:
    print ("ERROR")
