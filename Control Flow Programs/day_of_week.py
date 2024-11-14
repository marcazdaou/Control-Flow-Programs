import stdio
import sys

# accepts m (int), d (int), and y (int) as command-line arguments
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Write the day of the week (0 for Sunday, 1 for Monday, and so on) dow to standard output
y0 = y-(14 - m)//12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m)//12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Write dow to standard output

if dow == 0:
    stdio.writeln("Sunday")
elif dow == 1:
    stdio.writeln("Monday")
elif dow == 2:
    stdio.writeln("Tuesday")
elif dow == 3:
    stdio.writeln("Wednesday")
elif dow == 4:
    stdio.writeln("Thursday")
elif dow == 5:
    stdio.writeln("Friday")
else:
    stdio.writeln("Saturday")
