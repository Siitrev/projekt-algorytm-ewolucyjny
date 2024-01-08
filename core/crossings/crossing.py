import numpy as np

def crossing(genome1 : str, genome2: str, probabilityOfCrossing : int):
    random = np.random.randint(0,100)
    if (random <= probabilityOfCrossing):
        randomPoint =  np.random.randint(1, len(genome1)-1)
        tmp = genome1[randomPoint:]
        newGenome1 = genome1[:randomPoint] + genome2[randomPoint:]
        newGenome2 = genome2[:randomPoint] + tmp
        print(newGenome1 + " " + newGenome2)
        return (newGenome1, newGenome2)
    else:
        return (genome1, genome2)
