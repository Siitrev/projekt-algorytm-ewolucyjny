import numpy as np

def onePointCrossing(genome1 : str, genome2: str):

    random_point =  np.random.randint(1, len(genome1))
    tmp = genome1[random_point:]
    new_genome1 = genome1[:random_point] + genome2[random_point:]
    new_genome2 = genome2[:random_point] + tmp
    return (new_genome1, new_genome2)

    

def twoPointCrossing(genome1 : str, genome2: str):

    random_point =  np.random.randint(0, len(genome1))
    random_point2 = np.random.randint(random_point+1, len(genome1)+1)

    print("rp1: " + str(random_point) + ", rp2: " + str(random_point2))

    new_genome1 = genome1[:random_point] + genome2[random_point:random_point2] + \
    genome1[random_point2:]

    new_genome2 = genome2[:random_point] + genome1[random_point:random_point2] + \
    genome2[random_point2:]

    print(new_genome1 + " " + new_genome2)
    return (new_genome1, new_genome2)
    

def homogeneousCrossing(genome1 : str, genome2: str, probabilityOfCrossing : int):

    newGenome1 = ""
    newGenome2 = ""
    randomNumbers = []

    for x in range(int(len(genome1)/2)):
        randomNumbers.append(np.random.randint(0,100))
    
    randomNumbersCounter = 0

    for x in range(len(genome1)):

        if x % 2 == 1:
            if (randomNumbers[randomNumbersCounter] < probabilityOfCrossing ):
                newGenome1 += genome2[x]
                newGenome2 += genome1[x]
                randomNumbersCounter += 1
            else:
                newGenome1 += genome1[x]
                newGenome2 += genome2[x]
        if x % 2 == 0:
            newGenome1 += genome1[x]
            newGenome2 += genome2[x]

    return (newGenome1, newGenome2)