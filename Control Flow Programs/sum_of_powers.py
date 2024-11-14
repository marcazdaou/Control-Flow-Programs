import stdio
import sys

# accepts n (int) and k (int) as command-line arguments
n = int(sys.argv[1])
k = int(sys.argv[2])

# Set total to 0.
total = 0

# Repeat for each i ∈ [1, n]:
#  Increment total by i

for i in range(1, n+1):
    total += i ** k

# Write total (sum of powers).

stdio.writeln(total)
