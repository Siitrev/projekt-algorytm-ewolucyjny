import numpy as np

class ChromosomeInfo:
    def __init__(self, start : float, end : float, precision : int) -> None:
        self.start = start
        self.end = end
        self.precision = precision

class Chromosome:
    def __init__(self, chromosome_info : ChromosomeInfo) -> None:
        self.__end = chromosome_info.end
        self.__start = chromosome_info.start
        self.__precision = chromosome_info.precision
        self.m = np.ceil(np.log2((self.__end-self.__start)* \
            np.power(10,self.__precision)) + np.log2(1))
        self.randoms = [np.random.randint(0,2) for x in range(int(self.m))]
        self.genome = "".join([str(x) for x in self.randoms])
        
    def toNumber(self) -> float:
        addent = int(self.genome, 2) * (self.__end - self.__start)/(np.power(2,self.m) - 1)
        return self.__start + addent

class Person:
    def __init__(self, chromosome_info : ChromosomeInfo) -> None:
        self.chromosome = Chromosome(chromosome_info)
        
    def __str__(self) -> str:
        return str(self.chromosome.genome)

class Population:
    best_people = []
    def __init__(self, size : int, chromosome_info : ChromosomeInfo) -> None:
        self.people = [Person(chromosome_info) for _ in range(size)]

class Experiment:
    def __init__(self) -> None:
        pass
    
    def mutate(self, mutation):
        pass
    
    def inverse(self, inversion):
        pass
    
    def cross(self, crossing):
        pass
# mut = Mutation(n = 1)
# Experiment.mutate(mut)      
# for i in range(20):
#     Experiment.setBest()
#     Experiment.cross()
#     Experiment.mutate()
#     Experiment.inverse()
#     Experiment.nextEpoch()
# best = pop1.getBest()
# pop2 = Population(213- len(best))
# pop2.addPeople(best)