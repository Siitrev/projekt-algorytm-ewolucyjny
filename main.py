from core.template.template import *
from core.strategies.strategies import Strategy
from gui.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication
import benchmark_functions as bf
import sys

fitness_function = bf.Michalewicz()

info = ChromosomeInfo(-10, 10, 6)
pop = Population(10, info)
print(pop, "\n")
strategies = Strategy()
sample = strategies.best_selection(pop,6)
print(str(sample).replace("),",")\n"))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())
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
