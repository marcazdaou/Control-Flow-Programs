
import stdio
import sys

# accepts n (int) as command-line argument
n = int(sys.argv[1])
# Repeat for each i ∈ [2, n]:
# Set total (sum of divisors of i) to 0.
for i in range(2, n+1):
    total = 0

    for j in range(1, int(i/2)+1):
        if i % j == 0:
            total = total + j

    if i == total:
        stdio.writeln(i)
