import stdio
import sys

#  accepts n (int) as command-line argument
n = int(sys.argv[1])

# Set dragon and nogard to the string “F”.
dragon = "F"
nogard = "F"

# Repeat for each i ∈ [1, n]:
# Exchange dragon and nogard with dragon “L” nogard and dragon “R” nogard.
for i in range(1, n+1):
    (dragon, nogard) = (dragon + "L" + nogard, dragon+"R"+nogard)

stdio.writeln(dragon)
