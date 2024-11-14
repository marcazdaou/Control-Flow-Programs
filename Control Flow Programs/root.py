import stdio
import sys

# accepts k (int), c (float), and epsilon (float) as command-line arguments
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# set t to c
t = c
# Repeat as long as |1 − c/tk| > E:
# Replace t by t − f(t)/f0 (t), where f(t) = t ** k − c and f 0(t) = kt**k−1
# .
while abs(1 - (c / t ** k)) > epsilon:
    t = t - ((t ** k - c) / (k * t ** (k-1)))

# write t
stdio.writeln(t)
