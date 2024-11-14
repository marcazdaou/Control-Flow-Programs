import stdio
import sys

#  accepts p (int) and q (int) as command-line arguments
p = int(sys.argv[1])
q = int(sys.argv[2])

# Repeat as long as p mod q != 0:
# Exchange p and q with q and p mod q
while p % q != 0:
    (p, q) = (q, p % q)

#  Write q (the gcd).
stdio.writeln(q)
