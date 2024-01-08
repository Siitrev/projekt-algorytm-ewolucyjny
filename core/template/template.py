import numpy as np
from typing import Callable
import benchmark_functions as bf


class ChromosomeInfo:
    def __init__(self, start: float, end: float, precision: int) -> None:
        self.start = start
        self.end = end
        self.precision = precision


class Chromosome:
    def __init__(self, chromosome_info: ChromosomeInfo) -> None:
        self.__end = chromosome_info.end
        self.__start = chromosome_info.start
        self.__precision = chromosome_info.precision
        self.m = np.ceil(
            np.log2((self.__end - self.__start) * np.power(10, self.__precision))
            + np.log2(1)
        )
        self.m = int(self.m)
        self.randoms = [np.random.randint(0, 2) for _ in range(int(self.m))]
        self.genome = "".join([str(bit) for bit in self.randoms])

    def to_number(self) -> float:
        addent = (
            int(self.genome, 2)
            * (self.__end - self.__start)
            / (np.power(2, self.m) - 1)
        )
        return self.__start + addent
      
    def set(self, chromosome: str):
        self.genome = chromosome

    def get(self) -> str:
        return self.genome
    
    def __str__(self) -> str:
        return self.genome


class Person:
    def __init__(self, chromosome_info: ChromosomeInfo) -> None:
        self.fitness_function = bf.Michalewicz()
        self.chromosomes = (Chromosome(chromosome_info), Chromosome(chromosome_info))
        first_chromosome = self.chromosomes[0].to_number()
        second_chromosome = self.chromosomes[1].to_number()
        self.value = np.round(self.fitness_function([first_chromosome, second_chromosome]),self.chromosomes[0].m + 1)

    def __str__(self) -> str:
        return str(
            tuple([chromosome.to_number() for chromosome in self.chromosomes])
            + (self.value,)
        )

    def __repr__(self) -> str:
        return str(self)


class Population:
    def __init__(self, size: int, chromosome_info: ChromosomeInfo) -> None:
        self.people = [Person(chromosome_info) for _ in range(size)]
        self.best_people = []

    def set_best_people(self, amount: int = 1, descending=False):
        self.best_people = []
        temp = sorted(self.people, reverse=descending, key=lambda x: x.value)
        for person in temp[:amount]:
            self.best_people.append(person)

    def add_people(self, *people):
        self.people += people

    def remove_people(self, amount=1):
        for _ in range(amount):
            index = np.random.randint(0, len(self.people))
            self.people.pop(index)

    # def __str__(self) -> str:
    #     return str(self.people)

    def __repr__(self) -> str:
        temp = [
            tuple(
                [chromosome.to_number() for chromosome in person.chromosomes]
                + [person.value]
            )
            for person in self.people
        ]
        return str(temp).replace("),", ")\n")


class Experiment:
    def __init__(self, size: int, chromosome_info: ChromosomeInfo) -> None:
        self.population = Population(size, chromosome_info)

    def mutate(self, mutation: Callable, probability=0.3):
        for index, person in enumerate(self.population.people):
            chance = np.random.rand()

            if chance <= probability:
                new_chromosome_1 = mutation(person.chromosomes[0])
                new_chromosome_2 = mutation(person.chromosomes[1])
                
                self.population.people[index].chromosomes[0].set(new_chromosome_1)
                self.population.people[index].chromosomes[0].set(new_chromosome_2)

    def inverse(self, inversion: Callable, probability=0.1):
        for index, person in enumerate(self.population.people):
            chance = np.random.rand()

            if chance <= probability:
                new_chromosome_1 = inversion(person.chromosomes[0].get())
                new_chromosome_2 = inversion(person.chromosomes[1].get())
                
                self.population.people[index].chromosomes[0].set(new_chromosome_1)
                self.population.people[index].chromosomes[0].set(new_chromosome_2)

    def cross(self, crossing: Callable, probability=0.8):
        pass

    def selection(self, select_method: Callable, amount: float, maximization=False, **kwargs):
        if "contestants" in kwargs:
            return select_method(self.population, amount=amount, maximization=maximization, number_of_contestants = kwargs["contestants"])
        return select_method(self.population, amount=amount, maximization=maximization)
