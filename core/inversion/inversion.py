# Rdz 1, 3
import numpy as np


def inversion(chromosome : str) -> str:
    invert = {'0':'1', '1':'0'}
    inversion_points = np.random.randint(low=0, high=len(chromosome)+1, size=2)
    print(inversion_points)

    anaphase = [*chromosome]
    for i in range(*sorted(inversion_points)):
        anaphase[i] = invert[anaphase[i]]

    return ''.join(anaphase)

print(inversion("00110101010"))