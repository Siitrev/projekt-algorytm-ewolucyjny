from core.template.template import *
import benchmark_functions as bf


def fun(x):
    return 2*np.power(x,2) + 5
fitness_function = bf.Michalewicz()

info = ChromosomeInfo(-10,10,6)
pop = Population(50,info)
pop.set_best_people(2)
for person in pop.best_people:
    print(person.chromosome.to_number())