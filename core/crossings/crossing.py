import numpy as np

def crossing(genome1 : str, genome2: str):
    randomPoint =  np.random.randint(1, len(genome1))
    tmp = genome1[randomPoint:]
    new_genome1 = genome1[:randomPoint] + genome2[randomPoint:]
    new_genome2 = genome2[:randomPoint] + tmp
    return (new_genome1, new_genome2)
