import sys
import string

try:
    str = "".join(c for c in sys.argv[1] if c not in string.punctuation).split()
    n = int(sys.argv[2])
except ValueError:
    sys.exit("ERROR")

print ([word for word in str if len(word) > n])
