import stdio
import sys

#  accepts n (int) as command-line argument,
n = int(sys.argv[1])
a = 1

while a <= n**(1/3):
    # raise a to the power of 3
    a3 = a*a*a
    # a cannot be bigger than n

    if a > n:
        break
# set variable b equal to given bound (a +1)
    b = a + 1
    # use while loops for the bound
    while b <= n - a**3:
        # raise b to the power of 3
        b3 = b*b*b
        # a cubed + b cubed cannot be bigger than n
        if a3 + b3 > n:
            break
# set variable c = a + 1
        c = a + 1
        # use while loops to identify c
        while c <= n**(1/3):
            # raise c to power of 3
            c3 = c*c*c
            # c cubed cannot be bigger than a cubed and b cubed
            if c3 > a3 + b3:
                break
# set d to c + 1
            d = c + 1
            # use while loops for the given bound
            while d <= n - c**3:
                # raise d to the power of 3
                d3 = d*d*d
                # c cubed + d cubed cannot be bigger than a cubed and b cubed
                if c3 + d3 > a3 + b3:
                    break
                    #  writes to standard output a cubed + b cubed = c cubed + d cubed
                if a3 + b3 == c3 + d3:
                    stdio.write(str(a3 + b3) + " = ")
                    stdio.write(str(a) + "^3 + " + str(b) + "^3" + " = ")
                    stdio.writeln(str(c) + "^3 + " + str(d) + "^3")
                # increment d by 1
                d += 1
            # increment c by 1
            c += 1
        # increment b by 1
        b += 1
    # increment a by 1
    a += 1
