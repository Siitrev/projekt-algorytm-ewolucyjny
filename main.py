from core.template.template import *
import benchmark_functions as bf
import pprint as pp


def fun(x):
    return 2 * np.power(x, 2) + 5


fitness_function = bf.Michalewicz()

info = ChromosomeInfo(-10, 10, 6)
pop = Population(10, info)
print(pop)
for index, person in enumerate(pop.people):
    person.chromosome.set("0011111100101010101010001")
print(pop)
# mut = Mutation(n = 1)
# Experiment.mutate(mut)
# for i in range(20):
#     Experiment.population.set_best_people()
#     Experiment.cross()
#     Experiment.mutate()
#     Experiment.inverse()
#     Experiment.nextEpoch()
# best = pop1.getBest()
# pop2 = Population(213- len(best))
# pop2.addPeople(best)
