import sys

try:
    av = sys.argv[1].split(' ')
    n = int(sys.argv[2])
except ValueError:
    sys.exit("ERROR")

print ([w for w in av if len(w) > n])
