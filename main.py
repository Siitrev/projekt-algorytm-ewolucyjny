from core.template.template import *
import benchmark_functions as bf


def fun(x):
    return 2*np.power(x,2) + 5
fitness_function = bf.Michalewicz()

info = ChromosomeInfo(-10,10,6)
pop = Population(200,info)
[print(x) for x in pop.people]
print(fitness_function([2.202906,1.570796]))