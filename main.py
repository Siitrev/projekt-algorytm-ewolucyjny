from core.template.template import *
from core.strategies.strategies import *
from core.mutations.mutation import mutation

from gui.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication
import benchmark_functions as bf
import sys

# fitness_function = bf.Michalewicz()

# info = ChromosomeInfo(-30, 30, 6)
# ex = Experiment(5, info)

# print(ex.population, "\n")
# sample = ex.selection(roulette_wheel, 3)
# print(str(sample).replace("),",")\n"))

# old = pop.people[0].chromosomes[0]
# new = mutation(pop.people[0].chromosomes[0], 2)

# print(old.genome.count("1"), old.genome.count("0"))
# print(new.count("1"), new.count("0"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
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

#3.141592653589793
