#This script written by Matthew Henry for 44-608
#Logic and datastructures reconsidered to avoid excessive code for managing the 12 states to monitor
import random as random

def main():
    #I don't want to manage 12 variables and all those if statements.  I'll create a list of length 12 and use the indicies to update the individual counts
    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #set to a constant value for reproducible randomness
    random.seed(10)

    for roll in range(6000000):
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        Sum = die1 + die2
        frequency[Sum - 1] += 1 #correcting for lists being 0-indexed
    
    counter = 1
    print(f'Face{"Frequency":>13}')

    for count in frequency:
        print(f'{counter:>4}{count:>13}')
    
    craps = frequency[2 - 1] + frequency [3-1] + frequency[12 - 1]
    wins = frequency[7 - 1] + frequency[11 - 1]

    print(f'Craps: {craps/sum(frequency)}')
    print(f'Win: {wins/sum(frequency)}')


if __name__ == "__main__":
    main()