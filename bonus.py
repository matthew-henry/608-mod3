#Script by Matthew Henry
#A Monte Carlo Random Walk in 2-D space (evaluating distance traveled from center)
import random as random
import math as math
import statistics as stats
import pylab
import scipy.stats as scipy
import tqdm as tqdm

class randomWalker:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def walk(self):
        theta = 2*math.pi*random.random() # random orientation in radians
        stepsize = 5 * random.random()  # random stepsize between 0 and 5
        self.x += stepsize * math.cos(theta)
        self.y += stepsize * math.sin(theta) #basic trig

    def getDistance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2) #pythagorean theorem/Euclidean distance

def main():
    numWalkers = 10 ** 5
    numSteps = 10 ** 3
    walkerList = []
    distances = []
    for i in tqdm.tqdm(range(numWalkers), desc="Calculating...", ascii=False, ncols = 100):
        walkerList.append(randomWalker())
        for j in range(numSteps):
            walkerList[i].walk()
        distances.append(walkerList[i].getDistance())
    
    print(f'The mean distance from center traveled is {stats.mean(distances)}.')
    print(f'The median distance from center traveled is {stats.median(distances)}')
    print(f'The variance is {stats.variance(distances)}')
    print(f'The standard deviation is {stats.stdev(distances)}')
    scipy.probplot(distances, dist= "norm", plot=pylab) #test for normality out of curiousity
    pylab.show()
    
if __name__ == "__main__":
    main()    