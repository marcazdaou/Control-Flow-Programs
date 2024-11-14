import stdio
import sys

# accepts n (int) as command-line argument
n = int(sys.argv[1])

# Set a, b (the first two Fibonacci numbers) to 1, and i to 3.
a = 1
b = 1
i = 3

# Repeat as long as i ≤ n
#  Exchange a and b with b and a + b.
#  Increment i by 1.
while i <= n:
    (a, b) = (b, a+b)
    i += 1

# Write b (nth Fibonacci number).
stdio.writeln(b)
