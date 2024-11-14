import stdio
import sys

# Accepts t (float) and v (float) as command-line arguments
t = float(sys.argv[1])
v = float(sys.argv[2])

# d writes the wind chill w to standard output
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# report the message “Value of t must be ≤ 50 F” if t > 50
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")

# report the message “Value of v must be > 3 mph” if v ≤ 3.
elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")

# writes w to standard output
else:
    stdio.writeln(w)
