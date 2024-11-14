import stdio
import stdrandom

# Set rank to a random integer from [2, 14]
rank = stdrandom.uniformInt(2, 15)
rankStr = ()
# set rankStr to a string corresponding to rank — the ranks are 2, 3, . Jack, Queen, King, and Ace.

if rank == 2:
    rankStr = "2"
elif rank == 3:
    rankStr = "3"
elif rank == 4:
    rankStr = "4"
elif rank == 5:
    rankStr = "5"
elif rank == 6:
    rankStr = "6"
elif rank == 7:
    rankStr = "7"
elif rank == 8:
    rankStr = "8"
elif rank == 9:
    rankStr = "9"
elif rank == 10:
    rankStr = "10"
elif rank == 11:
    rankStr = "Ace"
elif rank == 12:
    rankStr = "Jack"
elif rank == 13:
    rankStr = "Queen"
else:
    rankStr = "King"

# Set suit to a random integer from [1, 4].
suit = stdrandom.uniformInt(1, 5)
suitStr = ()
# set suitStr to a string corresponding to suit — the suits are Clubs, Diamonds, Hearts, and Spades.

if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
else:
    suitStr = "Spades"

# Write the desired output.
stdio.writeln(rankStr + " of " + suitStr)
